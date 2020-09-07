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

class Game():

    def __init__(self):
        pygame.init()

        self.createScreen()

        self.makeTeam1()
        self.makeTeam2()

        self.setGameState()

        self.mainLoop()

    def createScreen(self):
        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)


    def makeTeam1(self):
        character1 = Character("AAA", 10, 100, 2, constants.INITIAL_PLAYER1_POS)

        self.team1 = [character1]

    def makeTeam2(self):
        character1 = Character("BBB", 12, 75, 7, constants.INITIAL_PLAYER2_POS)

        self.team2 = [character1]


    def setGameState(self):
        self.gameState = GameState(self.team1, self.team2)


    def mainLoop(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()




            self.screen.fill(colors.BACKGROUND)

            time.sleep(constants.TIME_DELAY)

            self.drawBoard()

            pygame.display.update()
            if not self.gameState.end:
                self.gameState.updatePos()


    def drawBoard(self):
        for i in range(constants.NUM_CELLS):
            for j in range(constants.NUM_CELLS):

                position = (i * constants.CELL_SIZE[0] + constants.OFFSET,
                            j * constants.CELL_SIZE[1] + constants.OFFSET,
                            constants.CELL_SIZE[0],
                            constants.CELL_SIZE[1])

                color = colors.CELL_BORDER
                border = 1

                pygame.draw.rect(self.screen, color, position, border)

                self.drawTeam1()
                self.drawTeam2()

    def drawTeam1(self):
        for character in self.gameState.team1:
            self.drawCharacter(character, colors.PLAYER1)

    def drawTeam2(self):
        for character in self.gameState.team2:
            self.drawCharacter(character, colors.PLAYER2)


    def drawCharacter(self, character, color):

        position = (character.position[0] * constants.CELL_SIZE[0] + constants.OFFSET,
                    character.position[1] * constants.CELL_SIZE[1] + constants.OFFSET,
                    constants.CELL_SIZE[0],
                    constants.CELL_SIZE[1])

        border = 0

        currentHealthPercent = character.health / character.maxHealth

        posHealthBarFull = (position[0] + constants.HEALTHBAR_OFFSET[0],
                            position[1] + constants.HEALTHBAR_OFFSET[1],
                            constants.HEALTHBAR_SIZE[0],
                            constants.HEALTHBAR_SIZE[1])
        posHealthBarCurrent = (position[0] + constants.HEALTHBAR_OFFSET[0],
                            position[1] + constants.HEALTHBAR_OFFSET[1],
                            constants.HEALTHBAR_SIZE[0] * currentHealthPercent,
                            constants.HEALTHBAR_SIZE[1])

        # Character
        pygame.draw.rect(self.screen, color, position, border)


        # HealthBar
        pygame.draw.rect(self.screen, colors.HEALTHBAR_BOTTOM, posHealthBarFull, border)
        pygame.draw.rect(self.screen, colors.HEALTHBAR_TOP, posHealthBarCurrent, border)
