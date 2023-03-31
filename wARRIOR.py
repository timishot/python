import random
import math
#Warrior & Bottle Class
class Warrior:

    def __init__(self, name="Warrior", health=0, attkmax=0, blockMax=0):
        self.name=name
        self.health=health
        self.attkmax=attkmax
        self.blockMax=blockMax

    def attack(self):
        attkAmt = self.attkmax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt
    
class Battle:

    def startFight(self,warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
            
    @staticmethod
    def getAttackResult(warriorA,warriorB):

        warriorAAttkAmt= warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2warriorB = math.ceil(warriorAAttkAmt-warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2warriorB

        print("{} attack {} and deals {} damage".format(warriorA.name, warriorB.name, damage2warriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} had Died and {} is victorious".format(warriorB.name, warriorA.name))


def main():
    maximus = Warrior("maxinum", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

main()
#They will have capabilities to attack and block random amounts

#Attack randoms() 0.0 to 1.0 * maxattack + .5

Block will use random()

#Bottle class capability of looping until 1 warrior dies
#warriors will each get a turn to attack each other

#function get 2 warriors
#1 warrior attack the other