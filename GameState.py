class GameState():

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

        self.end = False

        for character in self.team1:
            character.updateTeam(1)

        for character in self.team2:
            character.updateTeam(2)


    def getTeam1Pos(self):
        return list(map(lambda x: x.position, self.team1))

    def getTeam2Pos(self):
        return list(map(lambda x: x.position, self.team2))

    def updatePos(self):

        # Team 1
        for character in self.team1:
            currentPos = character.position
            direction = self.directionTo(currentPos, self.getClosestPositionTeam2(currentPos))

            # Characters can do only one acction (move or attack)

            if not self.characterCanAttack(character, direction):
                self.moveCharacter(character, currentPos, direction)


        # Team 2
        for character in self.team2:
            currentPos = character.position
            direction = self.directionTo(currentPos, self.getClosestPositionTeam1(currentPos))

            if not self.characterCanAttack(character, direction):
                self.moveCharacter(character, currentPos, direction)



    def moveCharacter(self, character, position, direction):
        if direction[0] != 0:
            directionSign = direction[0]/abs(direction[0])
            character.updatePosition((position[0] + directionSign, position[1]))
        elif direction[1] != 0:
            directionSign = direction[1]/abs(direction[1])
            character.updatePosition((position[0], position[1] + directionSign))

    def characterCanAttack(self, character, direction):

        if abs(direction[0]) + abs(direction[1]) <= character.range:
            enemy = None

            # Character of team 1
            if character.team == 1:
                enemy = self.getClosestCharacterTeam2(character.position)

            # Character of team 2
            else:
                enemy = self.getClosestCharacterTeam1(character.position)

            enemy.updateHealth(enemy.health - character.attack)

            if enemy.health == 0:
                self.killCharacter(enemy)

            return True

        return False

    def killCharacter(self, character):
        if character.team == 1:
            self.team1.remove(character)
            if len(self.team1) == 0:
                self.endGame()
        else:
            self.team2.remove(character)
            if len(self.team2) == 0:
                self.endGame()


    def endGame(self):
        self.end = True

    def getClosestPositionTeam1(self, position):

        min = 99999;
        closestPosition = None

        for element in self.getTeam1Pos():
            distance = self.manhattanDistance(position, element)
            if distance < min:
                minimum = distance
                closestPosition = element

        return closestPosition


    def getClosestCharacterTeam1(self, position):

        min = 99999;
        closestPosition = None

        for character in self.team1:
            distance = self.manhattanDistance(position, character.position)
            if distance < min:
                minimum = distance
                closestCharacter = character

        return closestCharacter

    def getClosestPositionTeam2(self, position):

        min = 99999;
        closestPosition = None

        for element in self.getTeam2Pos():
            distance = self.manhattanDistance(position, element)
            if distance < min:
                minimum = distance
                closestPosition = element

        return closestPosition

    def getClosestCharacterTeam2(self, position):

        min = 99999;
        closestPosition = None

        for character in self.team2:
            distance = self.manhattanDistance(position, character.position)
            if distance < min:
                minimum = distance
                closestCharacter = character

        return closestCharacter

    def manhattanDistance(self, position1, position2):
        return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

    def directionTo(self, position1, position2):
        return (position2[0] - position1[0], position2[1] - position1[1])
