class Character():

    def __init__(self, name, attack, health, range, position):
        self.name = name
        self.attack = attack
        self.health = health
        self.maxHealth = health
        self.range = range
        self.position = position
        self.team = None

    def updatePosition(self, newPosition):
        self.position = newPosition

    def updateTeam(self, newTeam):
        self.team = newTeam

    def updateHealth(self, newHealth):
        if newHealth <= 0:
            self.health = 0
        else:
            self.health = newHealth
