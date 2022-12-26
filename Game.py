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

    def move_player(self, move):
        if move == "UP":
            x = 0
        elif move == "DOWN":
            x = 1
        elif move == "LEFT":
            x = 2
        elif move == "RIGHT":
            x = 3