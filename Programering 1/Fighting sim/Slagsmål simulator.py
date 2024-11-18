import time
import sys
from SlowPrint import slowPrint
from random import randint
import threading

def main():
    
    # Timing for slowPrint function
    textFast = 0.001
    textSlow = 0.5

    class fighter:
        def __init__(self, name, age, health, speed, maxDamage):
            self.name = name
            self.age = age
            self.health = health
            self.speed = speed
            self.maxDamage = maxDamage
            self.lock = threading.Lock()  # Lock to prevent race conditions when both fighters attack

        def __str__(self):
            return f"{self.name} \nage: {self.age} \nHP: {self.health} \nSpeed: {self.speed}\n"

        def hit_enemy(self, other_fighter):
            while self.health > 0 and other_fighter.health > 0:
                with self.lock:  # Ensure that only one fighter attacks at a time
                    damage = randint(5, self.maxDamage)
                    other_fighter.health -= damage

                    # Small check to not fight when dead
                    if self.health <= 0:
                        break
                
                    # Sleep based on fighter's speed for attack timing
                    time.sleep(2 if self.speed == 'slow' else 1)

                    slowPrint(f"{self.name} hits {other_fighter.name} for {damage} damage", textFast)
                    slowPrint(f"{other_fighter.name} is now at {other_fighter.health} HP", textFast)
                    print()
                    time.sleep(1)

                # Stop attacking if either fighter is down
                if other_fighter.health <= 0:
                    slowPrint(f"{other_fighter.name} has been defeated!")
                    slowPrint(f"{self.name} is crowned winner!")
                    break

                # Sleep based on fighter's speed for attack timing
                time.sleep(2.5 if self.speed == 'slow' else 1)

    #Hard coded stats of fighters
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


    # Create threads for both fighters to attack each other
    fighter1_thread = threading.Thread(target=fighter1.hit_enemy, args=(fighter2,))
    fighter2_thread = threading.Thread(target=fighter2.hit_enemy, args=(fighter1,))

    # Start the threads
    fighter1_thread.start()
    fighter2_thread.start()


    fighter1_thread.join()
    fighter2_thread.join()
        
    
if __name__ == "__main__":
    main()