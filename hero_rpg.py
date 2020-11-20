#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. fleeasdaksjdhasdjk
# class Character:
#     def __init__(self, name, health, power):
#         self.health = health
#         self.power = power
#         self.name = name
    
#     def attack(self, enemy):
#         Hero attacks goblin
#         enemy.health -= self.power
#         self.__class__.__name__

#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
    
#     def print_status(self):
#         print(f"{self.name} has {self.health} health and {self.power} power.")

# class Hero:
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
    
#     def attack(self, enemy):
#         # Hero attacks goblin
#         enemy.health -= self.power
    
#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
    
#     def print_status(self):
#         print("You have {} health and {} power.".format(self.health, self.power))

    
        

# class Goblin:
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
    
#     def attack(self, enemy):
#         # Goblin attacks hero
#         enemy.health -= self.power
    
#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
    
#     def print_status(self):
#         print("The goblin has {} health and {} power.".format(self.health, self.power))

    


# def main():
#     hero = Character("Hero", 10, 5)
#     goblin = Character("Goblin", 6, 2)
#     zombie = Character("Zombie", 6, 2)

#     while goblin.alive() and hero.alive(): #and zombie.alive():
#         hero.print_status()
#         goblin.print_status()
#         zombie.print_status()
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("4. fight zombie")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             Hero attacks goblin
#             hero.attack(goblin)
#             print(f"You do {hero.power} damage to the goblin.")
#             if not goblin.alive():
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "4":
#             hero.attack(zombie)
#             if not goblin.alive():
#                 print("The goblin is dead.")
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print(f"Invalid input {raw_input}")

#         if goblin.alive():
#             goblin.attack(hero)
#             print(f"The goblin does {goblin.power} damage to you.")
#             if not hero.alive():
#                 print("You are dead.")
        
#         if zombie.alive():
#             zombie.attack(hero)
#             print(f"The goblin does {zombie.power} damage to you.")
#             if not hero.alive():
#                 print("You are dead.")

# main()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    
    # def attack(self, enemy):
    #     # Hero attacks goblin
    #     enemy.health -= self.power

    def attack(self, enemy):
        # Hero attacks goblin
        if enemy.character_name != "zombie":
            enemy.health -= self.power

        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin" or self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")


class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power)

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power)

hero = Hero( 10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)

def main(enemy):

    while enemy.alive() > 0 and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)

            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.alive():
            enemy.attack(hero)
            if not hero.alive():
                print("You are dead.")

main(zombie)
