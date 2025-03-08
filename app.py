from models.robot import Robot
from models.owner import Owner

def main():
    robot_1 = Robot('Wall-e', 2110, 2000)
    robot_2 = Robot('EVA', 2805, 50000)

    robot_2.switch_ia_status()
    owner = Owner('BnL', robot_2)
    Robot.list_robots()
    print(owner)

if __name__ == "__main__":
    main()