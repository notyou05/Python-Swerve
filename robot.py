import wpilib.drive
import Constants
from Constants import driver_controller
from Easy_Swerve import joystick_input

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.driverController = wpilib.XboxController(driver_controller)


    def teleopPeriodic(self):
        left_joystick_x = -self.driverController.getLeftX(),
        left_joystick_y = -self.driverController.getRightY()
        right_joystick_x =  -self.driverController.getRightX()

        joystick_input(left_joystick_x, left_joystick_y, right_joystick_x)
