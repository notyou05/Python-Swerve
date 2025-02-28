import SwerveModule
from Constants import *  # Make sure the path to Constants.py is correct
from Easy_Swerve import joystick_input
from navx import AHRS
from robot import *


class SwerveDrive:
    def __init__(self) -> None:
        # Initialize swerve module instances
        self.frontLeft = SwerveModule.SwerveModule(Front_left_Drive_Id, Front_left_Steer_Id, Front_left_Encoder_Id, Front_left_Encoder_Offset)
        self.frontRight = SwerveModule.SwerveModule(Front_right_Drive_Id, Front_right_Steer_Id, Front_right_Encoder_Id, Front_right_Encoder_Offset)
        self.backLeft = SwerveModule.SwerveModule(Back_left_Drive_Id, Back_left_Steer_Id, Back_left_Encoder_Id, Back_left_Encoder_Offset)
        self.backRight = SwerveModule.SwerveModule(Back_right_Drive_Id, Back_right_Steer_Id, Back_right_Encoder_Id, Back_right_Encoder_Offset)




    def get_gyro_angle(self, navx_device: AHRS) -> float:
        angle = navx_device.getYaw()  # Yaw is in the range [-180, 180]
        return (angle + 360) % 360  # Convert to [0, 360)

    print(robot_centric_angle_to_drive)


