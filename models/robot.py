from datetime import datetime

class Robot:
    robots = []
    def __init__(self, name, year, value):
        self.id = int(datetime.now().timestamp() * 1_000_000)
        self.name = name
        self.year = year
        self.value = value
        self._has_ia = False
        Robot.robots.append(self)

    def __str__(self):
        return f'Name: {self.name.ljust(25)}, Year: {self.year}, Value: R${self.value}, Has IA: {self.has_ia}'

    @classmethod    
    def list_robots(cls):
        for robot in cls.robots:
            print(f'Name: {robot.name.ljust(25)}, Year: {robot.year}, Value: R${robot.value}, Has IA: {robot.has_ia}')
    
    @property
    def has_ia(self):
        return 'Habilitado' if self._has_ia else 'Desabilitado'
    
    def switch_ia_status(self):
        self._has_ia = not self._has_ia