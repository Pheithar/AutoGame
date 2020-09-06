# Bibliotecas
import numpy as np
import pygame
import sys
import time

# Constantes
import colors
import constants

# Clases
from GameState import GameState
from Character import Character

pygame.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)

character1 = Character("AAA", 10, 100, 2, constants.INITIAL_PLAYER1_POS)
character2 = Character("BBB", 12, 75, 7, constants.INITIAL_PLAYER2_POS)

gameState = GameState([character1], [character2])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()




    screen.fill(colors.BACKGROUND)

    time.sleep(0.1)

    for i in range(constants.NUM_CELLS):
        for j in range(constants.NUM_CELLS):

            position = (i * constants.CELL_SIZE[0],
                        j * constants.CELL_SIZE[1],
                        constants.CELL_SIZE[0],
                        constants.CELL_SIZE[1])

            color = colors.CELL_BORDER
            border = 1

            if (i, j) in gameState.getTeam1Pos():
                color = colors.PLAYER1
                border = 0
            elif (i, j) in gameState.getTeam2Pos():
                color = colors.PLAYER2
                border = 0

            pygame.draw.rect(screen, color, position, border)

    pygame.display.update()
    if not gameState.end:
        gameState.updatePos()   
