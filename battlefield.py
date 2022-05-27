from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon 
dinosaur = Dinosaur
robot = Robot
weapon = Weapon

class Battlefield:
    def __init__(self):
        self.name = "battlefield_one"
        self.robot = Robot ("Mr. Robot")
        self.dinosaur = Dinosaur("Trex", 40)
        self.weapon = Weapon("Laser", 30)
        
    
    def battle_phase(self):
        self.robot.attack_dinosaur(self.dinosaur)

    def run_game(self):
        print("The game has begun")
        pass
        






    