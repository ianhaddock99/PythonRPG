
import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy, double_power):
        doNotAttack = False
        if enemy.character_name == "shadow":
            enemy.shadow_dodge()
            doNotAttack = enemy.dodge

        if enemy.character_name == "warrior":
            berserk = random.random() > 0.2
            rnddmg =random.randint(1,11)
            if berserk == True:
                hero.health -= rnddmg
                print(f"Berserker rage, {rnddmg} extra damage done to hero.")

        if enemy.character_name == "medic":
            firstaid = random.random() > 0.8
            if firstaid:
                enemy.health += 2
                print("Medic has healed for 2 health.")
                
        if doNotAttack == False:
            if double_power == True:
                enemy.health -= (self.power * 2)
            else:
                enemy.health -= self.power

        if(self.character_name == "hero"):
            if double_power == True:
                print(f"You do {self.power * 2} damage to the {enemy.character_name}.")
            else:    
                print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif(self.character_name == "goblin" or self.character_name == "zombie" or self.character_name == "medic" or self.character_name == "shadow" or self.character_name == "warrior"):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin" or self.character_name == "zombie" or self.character_name == "medic" or self.character_name == "shadow" or self.character_name == "warrior":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")


class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power)

    def apply(self):
        hero.health += 10
        print("Hero health increased by 10.")

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power)

    def alive(self):
        return True

class Medic(Character):
    def __init__(self, health, power):
        self.character_name = "medic"
        super(Medic, self).__init__(health, power)

class Shadow(Character):
    dodge = False
    def __init__(self, health, power):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power)

    def shadow_dodge(self):    
        shadowdodge = random.random() > 0.1
        if shadowdodge:
            print("Shadow has dodged your attack.")
            self.dodge = True
        else:
            self.dodge = False   

class Warrior(Character):
    def __init__(self, health, power):
        self.character_name = "warrior"
        super(Warrior, self).__init__(health, power)


hero = Hero(100, 2)
goblin = Goblin(100, 2)
zombie = Zombie(10, 1)
shadow = Shadow(100, 2)
medic = Medic(100, 1)
warrior = Warrior(100, 2)

def main(enemy):

    while enemy.alive() > 0 and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy.character_name}")
        print("2. Do Nothing")
        print("3. Use Tonic")
        print("4. Flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            double_power = random.random() > 0.8
            hero.attack(enemy, double_power)

            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            hero.apply()
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.alive():
            enemy.attack(hero, False)
            if not hero.alive():
                print("You are dead.")

main(warrior)
