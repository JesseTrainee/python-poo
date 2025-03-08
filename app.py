from models.robot import Robot
from models.robotwithia import RobotWithIA
from models.owner import Owner

def main():
    robot_1 = Robot('Walle', 2110, 2000)
    robot_2 = RobotWithIA('EVA', 2805, 5000, 'Data analyse')

    robot_2.switch_ia_status()
    owner = Owner('BnL', robot_2)
    Robot.list_robots()
    print(owner)

if __name__ == "__main__":
    main()