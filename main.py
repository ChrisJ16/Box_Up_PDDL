import re

import pygame
import sys

from Game import Game

#Config
pygame.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planning")

WHITE = (255,255,255)
KINDABLACK = (30,30,30)
GRAY = (215, 215, 215)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255, 0, 0)

FPS = 60

font = pygame.font.SysFont('Arial', 30)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        WIN.blit(self.buttonSurface, self.buttonRect)

def myFunctionButton():
    print('Button Pressed')

#customButton = Button(50, 30, 200, 50, 'Button One', myFunctionButton)

def draw_empty_block(x, y):
    pygame.draw.rect(WIN,BLACK, (x,y,100,100), width=2)

def draw_full_block(x, y, size):
    pygame.draw.rect(WIN, BLACK, (x, y, size, size), width=0)

# size = 100(bloc full), ... 30(player)
def draw_box(x, y, size, colour, opening):
    gros = 4
    if opening == 1: #N
        #pygame.draw.lines(WIN, RED, False, [(200, 200), (200, 300), (300, 300), (300, 200)], 3)
        pygame.draw.lines(WIN, colour, False, [(x, y), (x, y+size), (x+size, y+size), (x+size, y)], gros)
    elif opening == 2: #V
        pygame.draw.lines(WIN, colour, False, [(x, y), (x+size, y), (x+size, y+size), (x, y+size)], gros)
    elif opening == 3: #S
        pygame.draw.lines(WIN, colour, False, [(x, y), (x, y+size)], gros)
        pygame.draw.lines(WIN, colour, False, [(x, y), (x+size, y), (x+size, y+size)], gros)
    elif opening == 4: #E
        pygame.draw.lines(WIN, colour, False, [(x, y), (x+size, y)], gros)
        pygame.draw.lines(WIN, colour, False, [(x, y), (x, y+size), (x+size, y + size)], gros)

def draw_playArea(rows, collumns, grid):
    (cX, cY) = (50, 50)
    for i in range(0, rows):
        for j in range(0, collumns):
            draw_empty_block(cX, cY)
            cX += 100
        cY += 100
        cX = 50

    (cX, cY) = (50, 50)
    for obj in grid:
        (objects, pos) = obj
        objList = re.split("-", objects)
        for auxObj in objList:
            if auxObj == 'p':
                draw_full_block(cX + 35, cY + 35, 30)
            elif auxObj == 'f':
                draw_full_block(cX, cY, 100)
            elif auxObj[0] != 'e':
                colour = WHITE
                size = 0
                (oX, oY) = (0,0)
                opening = auxObj[1]
                if auxObj[0] == 'r':
                    colour = RED
                    size = 50
                    (oX, oY) = (25,25)
                elif auxObj[0] == 'a':
                    colour = BLUE
                    size = 80
                    (oX, oY) = (10, 10)
                elif auxObj[0] == 'b':
                    colour = BLACK
                    size = 50
                    (oX, oY) = (25, 25)
                elif auxObj[0] == 'B':
                    colour = BLACK
                    size = 80
                    (oX, oY) = (10, 10)
                draw_box(cX + oX, cY + oY, size, colour, int(opening))
        cX += 100
        if cX >= collumns * 100:
            cY += 100
            cX = 50

def draw_window():
    pygame.display.update()
    WIN.fill(GRAY)

def main():
    clock = pygame.time.Clock()
    #run = True

    game = Game
    game.init_game(game, "level1")

    while True:
        clock.tick(FPS)
        # checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Up")
                    game.move_player(game, "UP", game.get_player_pos(game))
                elif event.key == pygame.K_DOWN:
                    print("Down")
                    game.move_player(game, "DOWN", game.get_player_pos(game))
                elif event.key == pygame.K_LEFT:
                    print("Left")
                    game.move_player(game, "LEFT", game.get_player_pos(game))
                elif event.key == pygame.K_RIGHT:
                    print("Right")
                    game.move_player(game, "RIGHT", game.get_player_pos(game))
                print(game.grid)
        # processing objects
        for object in objects:
            object.process()
        # redraw window
        draw_playArea(game.rows, game.columns, game.grid)
        draw_window()

# ne asiguram ca doar fisierul main
if __name__ == "__main__":
    main()