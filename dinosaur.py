class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack_robot(self, robot):
        robot.health -= self.attack_power
        print(f"{robot.name} health is now {robot.health}")
    

        