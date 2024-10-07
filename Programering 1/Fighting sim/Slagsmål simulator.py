import time
import sys
from SlowPrint import slowPrint
from random import randint

def main():
    
    textFast = 0.01
    textSlow = 0.5

    class fighter:
        def __init__(self, name, age, health, speed, maxDamage):
            self.name = name
            self.age = age
            self.health = health
            self.speed = speed
            self.maxDamage = maxDamage

        def hitEnemy(self, otherFighter, maxDamage):

            damage = randint(5, self.maxDamage)

            otherFighter.health -= damage
            
            return damage
            

        def __str__(self):
            return f"{self.name} \nage: {self.age} \nHP: {self.health} \nSpeed: {self.speed}\n"

    fighter1 = fighter('John Fight', 36, 110, 'slow', 20)
    fighter2 = fighter('Jack Duel', 24, 90, 'fast', 13)



    slowPrint(str(fighter1))
    time.sleep(1)
    print()
    slowPrint(str(fighter2))
    time.sleep(1)

    slowPrint('BEGIN', textSlow)
    time.sleep(1)
    print()

    while fighter1.health and fighter2.health > 0:

        damage_dealt = fighter1.hitEnemy(fighter2, fighter1.maxDamage)
        slowPrint(f"{fighter1.name} hits {fighter2.name} for {damage_dealt} damage", textFast)
        slowPrint(f"{fighter2.name} is now at {fighter2.health} HP", textFast)
        time.sleep(1)
        print()
        damage_dealt = fighter2.hitEnemy(fighter1, fighter2.maxDamage)
        slowPrint(f"{fighter2.name} hits {fighter1.name} for {damage_dealt} damage", textFast)
        slowPrint(f"{fighter1.name} is now at {fighter1.health} HP", textFast)
        time.sleep(1)
        print()
        
    
if __name__ == "__main__":
    main()
