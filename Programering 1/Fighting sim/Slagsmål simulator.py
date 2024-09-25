import time
import sys
import SlowPrint
from random import randint

class fighter:
    def __init__(self, name, age, health, speed, upperDamage):
        self.name = name
        self.age = age
        self.health = health
        self.speed = speed
        self.upperDamage = upperDamage

    def hitEnemy(self, otherFighter, upperDamage):

        damage = randint(5, self.upperDamage)

        otherFighter.health -= damage
        
        return damage
        

    def __str__(self):
        return f"{self.name} \nage: {self.age} \nHP: {self.health} \nSpeed: {self.speed}\n"

fighter1 = fighter('John Fight', 36, 110, 'slow', 20)
fighter2 = fighter('Jack Duel', 24, 90, 'fast', 12)



SlowPrint.slowPrint(str(fighter1))
print()
SlowPrint.slowPrint(str(fighter2))


for i in range(6):

    damage_dealt = fighter1.hitEnemy(fighter2, fighter1.upperDamage)
    SlowPrint.slowPrint(f"{fighter1.name} hits {fighter2.name} for {damage_dealt} damage")
    SlowPrint.slowPrint(f"{fighter2.name} is now at {fighter2.health} HP")

    damage_dealt = fighter2.hitEnemy(fighter1, fighter2.upperDamage)
    SlowPrint.slowPrint(f"{fighter2.name} hits {fighter1.name} for {damage_dealt} damage")
    SlowPrint.slowPrint(f"{fighter1.name} is now at {fighter1.health} HP")