import time
from typing import Optional
from models.robot import Robot

class Owner:
    def __init__(self, name, robot: Optional[Robot]):
        self.name = name
        self.robot = robot
        self.ownership_date = time.time()
    
    def __str__(self):
        return f'Owner Name: {self.name.ljust(10)} | Robot Name: {self.robot.name}'