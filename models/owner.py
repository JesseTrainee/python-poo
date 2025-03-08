from datetime import datetime
from typing import Optional
from models.robot import Robot

class Owner:
    def __init__(self, name, robot: Optional[Robot]):
        if not robot:
            raise ValueError("An owner must have a robot")
        self.name = name
        self.robot = robot
        self.ownership_date = datetime.now()

    def __str__(self):
        return f'Owner Name: {self.name.ljust(5)} | Robot Name: {self.robot.name.ljust(5)} | Ownership Date: {self.ownership_date.strftime("%d/%m/%Y %H:%M:%S")}'