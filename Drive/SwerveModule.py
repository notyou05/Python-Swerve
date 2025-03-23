import phoenix6
import math
from phoenix6 import hardware, controls
import Constants


class SwerveModule:
    def __init__(
        self,
        driveMotorID: int,
        turningMotorID: int,
        CANcoderID: int,
        CanCoderOffset: int,
    ) -> None:
        self.driveMotor = hardware.TalonFX(driveMotorID)
        self.turningMotor = hardware.TalonFX(turningMotorID)
        self.turningEncoder = hardware.CANcoder(CANcoderID)

    def getState(self):
        """Returns the current state of the swerve module."""
        return None  # Replace with actual implementation



    def setDesiredState(self, state):
        """Sets the desired state of the swerve module."""
        pass  # Replace with actual implementation




    def calculate_drive_speed(self):
        motor_rps = self.driveMotor.getVelocity().value  # Get motor RPS
        wheel_rps = motor_rps / Constants.DriveGearRatio  # Adjust for gear ratio

        # Calculate the linear velocity in m/s
        velocity_meter_per_second = 2 * math.pi * Constants.wheel_diameter * wheel_rps
        return velocity_meter_per_second

    def getPosition(self):
        return [1,1]



