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

    def move_player(self, move, player):
        (pl, pos) = player
        (pos1, pos2) = pos
        oldPos = pos
        outDir = -1
        inDir = -1
        if move == "UP":
            newPos = (pos1-1, pos2)
            outDir = 1
            inDir = 3
        elif move == "DOWN":
            newPos = (pos1+1, pos2)
            outDir = 3
            inDir = 1
        elif move == "LEFT":
            newPos = (pos1, pos2-1)
            outDir = 2
            inDir = 4
        elif move == "RIGHT":
            newPos = (pos1, pos2+1)
            outDir = 4
            inDir = 2

        k = 0
        nextObj = ""
        oldObj = ""
        #luam obiectele de pe vechea pozitie
        for obj in self.grid:
            (objects, position) = obj
            if oldPos == position:
                oldObj = objects
        # luam obiectele de pe noua pozitie
        for obj in self.grid:
            (objects, position) = obj
            if newPos == position:
                nextObj = objects

       # verificam cine iese: doar jucatorul sau si alte cutii
        aux = re.split("-", oldObj)
        newItem = ""
        leftItem = ""
        if aux[0] == 'p':
            finalOldObj = 'p'
        else:
            for item in aux:
                if item[0]!='e':
                    if item[0] != 'p':
                        if int(item[1]) != outDir:
                            newItem += item + "-"
                        else:
                            leftItem += item + "-"
            newItem += "p"
            if leftItem == "":
                leftItem = 'e'
            else:
                leftItem = leftItem[:-1]
            finalOldObj = newItem

        # verificam daca sse poate intra pe noua pozitie
        aux = re.split("-", nextObj)
        if aux[0] == 'e':
            finalNewObj = finalOldObj
        elif aux[0] != 'f' and not aux:
            auxP = re.split("-", finalOldObj)
            # verificam orientarea cutiei unde vor intra celelalte
            print(aux)
            if inDir == int(aux[0][1]):
                # verificam daca cutiile sunt compatibile
                # print(aux[0][0], auxP[0][0])
                if aux[0][0] == 'B' and (auxP[0][0] == 'B' or auxP[0][0] == 'a'):
                    print("impossible")
                    return
                elif aux[0][0] == 'a' and (auxP[0][0] == 'B' or auxP[0][0] == 'a'):
                    print("impossible")
                    return
                elif aux[0][0] == 'r' and (auxP[0][0] == 'b'):
                    print("impossible")
                    return
                elif aux[0][0] == 'b' and (auxP[0][0] == 'b'):
                    print("impossible")
                    return
                else:
                    print("du-te pornit")
                    finalNewObj = nextObj + "-" + finalOldObj

        grid = self.grid
        #acutalizam noua pozitie cu obiectele aferente
        for item in grid:
            (objects, position) = item
            if newPos == position:
                grid[k] = (finalNewObj, newPos)
            k += 1
        #acutalizam vechea pozitie cu obiectele aferente
        k=0
        for item in grid:
            (objects, position) = item
            if oldPos == position:
                grid[k] = (leftItem, newPos)
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