from datetime import datetime

class Robot:
    robots = []

    def __init__(self, name, year, value):
        """
        Inicializa a instância do robô.
        """
        if year < 1900:
            raise ValueError("Year must be valid")
        if year < 0:
            raise ValueError("Year can't be negative")

        self.id = self.generate_id()
        self.name = name
        self.year = year
        self.value = value
        Robot.robots.append(self)

    def __str__(self):
        return f'Name: {self.name.ljust(25)}, Year: {self.year}, Value: R${self.value}'

    @classmethod
    def list_robots(cls):
        """
        Retorna uma lista de robôs
        """
        for robot in cls.robots:
            print(robot)

    @staticmethod
    def generate_id():
        return int(datetime.now().timestamp() * 1_000_000)
