from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.name = "battlefield_one"
        self.robot = Robot ("Mr. Robot")
        self.dinosaur = Dinosaur("Trex", 40)
        


    def run_game(self):
        self.display_welcome()
        print("The game has begun")
        self.battle_phase()
        self.display_winner()
        pass

        
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            pass

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")
        pass

    def display_winner(self):
        if self.robot.health > 0:
            print("Mr. Robot has won the game!")
        elif self.dinosaur.health > 0:
            print("Trex has won the game!")
            pass
        






    