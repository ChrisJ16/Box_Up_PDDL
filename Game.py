import re

class Game:

    def __init__(self):
        self.rows = -1
        self.columns = -1
        self.grid = []

    def init_game(self, level):
        f = open(f"Levels/{level}", "r")
        aux = f.readline()
        (self.rows, self.columns) = (int(aux[0]), int(aux[2]))
        items = re.split("\s", f.read())
        items.pop()

        auxItems = []
        (i,j,k) = (0,0,0)
        (r,c) = (self.rows, self.columns)
        for obj in items:
            auxItems += [(items[k], (i,j))]
            k += 1
            j += 1
            if j == c:
                i += 1
                j =0
        self.grid = auxItems

    def get_player_pos(self):
        for obj in self.grid:
            (objects, pos) = obj
            aux = re.split("-", objects)
            for ax in aux:
                if ax == 'p':
                    return obj
        return None

    def get_pos_info(self, row, col):
        for obj in self.grid:
            (objects, pos) = obj
            if pos == (row, col):
                return objects
        return None

    def move_player(self, move, player):

        grid = self.grid
        (p, pos) = player
        (oldRow, oldCol) = pos
        (row, col) = (oldRow, oldCol)

        openings = ["UP", "LEFT", "DOWN", "RIGHT"]
        if move == "UP":
            row -= 1
        elif move == "DOWN":
            row += 1
        elif move == "LEFT":
            col -= 1
        elif move == "RIGHT":
            col += 1
        else:
            row = -1
            col = -1

        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            return self.grid
        else:
            # in primul si primul rand verificam daca putem face o miscare valida
            auxObj1 = re.split("-", self.get_pos_info(self, oldRow, oldCol)).pop() # poz veche
            auxObj2 = re.split("-", self.get_pos_info(self, row, col)).pop() # poz noua

            if auxObj1[0] == auxObj2[0]:
                print("problem")
            elif auxObj1[0] == 'B' and auxObj2[0] != 'e':
                print("problem")
            elif auxObj1[0] == 'a' and auxObj2 != 'e':
                print("problem")
            elif auxObj1[0] == 'b' and auxObj2 == 'r':
                print("problem")
            elif auxObj1[0] == 'r' and auxObj2 == 'b':
                print("problem")
            elif auxObj2 == 'f':
                print("problem")
            else:
                # luam itemele de pe vechea pozitie
                for ax in grid:
                    (auxItem, pos) = ax
                    if pos == (oldRow, oldCol):
                        item = auxItem
                # verificam ce iteme raman si care pleaca:
                oldItems = re.split("-", item)
                newItem = []
                leftItem = []
                while oldItems:
                    popped = oldItems.pop()
                    if popped == 'p':
                        newItem += [popped]
                    else:
                        if openings[int(popped[1])-1] != move:
                            newItem += [popped]
                        elif openings[int(popped[1])-1] == move and len(newItem) != 0:
                            newItem += [popped]
                        else:
                            leftItem += [popped]
                newItem.reverse()
                # verificam ce iteme pot intra pe noua pozitie, care nu
                # sunt trimise inapoi pe vechea pozitie, adica vor fi adaugate la oldItems
                itemsInNewPos = []
                for ax in grid:
                    (auxItem, pos) = ax
                    if pos == (row, col):
                        item = auxItem
                if item == 'e':
                    itemsInNewPos  = newItem
                else:
                    itemsInNewPos = re.split("-", item)
                    while newItem:
                        popped = newItem.pop()
                        if popped == 'p':
                            itemsInNewPos.insert(0, 'p')
                        else:
                            itemsInNewPos.insert(0, popped)
                # acum facem actualizarile in grid pe pozitia noua
                newItemString = ""
                while itemsInNewPos:
                    newItemString += itemsInNewPos.pop(0) + "-"
                newItemString = newItemString[:-1]

                oldItemString = ""
                if leftItem:
                    while leftItem:
                        oldItemString += leftItem.pop() + "-"
                    oldItemString = oldItemString[:-1]
                else:
                    oldItemString = 'e'
                #print("Itemele lasate pe vechea pozitie:", oldItemString)
                #print("Itemele de pe noua pozitie:", newItemString)

                k=0
                for ax in grid:
                    (auxItem, pos) = ax
                    if pos == (row, col):
                        grid[k] = (newItemString, (row, col))
                    elif pos == (oldRow, oldCol):
                        grid[k] = (oldItemString, (oldRow, oldCol))
                    k += 1
        self.grid = grid

    def is_goal_state(self):
        (trueBlue, trueRed) = (False, False)
        for obj in self.grid:
            (objects, pos) = obj
            aux = re.split("-", objects)
            for ax in aux:
                if ax[0] == 'a':
                    trueBlue = True
                if ax[0] == 'r':
                    trueRed = True
            if trueRed and trueBlue:
                return True
            (trueBlue, trueRed) = (False, False)
        return False