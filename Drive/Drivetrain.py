

import math
import wpilib
import wpimath.geometry
import wpimath.kinematics
import ntcore
from wpimath.kinematics import SwerveModuleState
from Drive.SwerveModule import SwerveModule  # Ensure this import is correct

kMaxSpeed = 5.0  # 3 meters per second
kMaxAngularSpeed = math.pi  # 1/2 rotation per second


class Drivetrain:


    def __init__(self) -> None:

        # to do fix numbers
        self.frontLeftLocation = wpimath.geometry.Translation2d(0.381, 0.381)
        self.frontRightLocation = wpimath.geometry.Translation2d(0.381, -0.381)
        self.backLeftLocation = wpimath.geometry.Translation2d(-0.381, 0.381)
        self.backRightLocation = wpimath.geometry.Translation2d(-0.381, -0.381)
        # to do: fix numbers
        self.frontLeft = SwerveModule(0, 0, 0, 0)
        self.frontRight = SwerveModule(0, 0, 0, 0)
        self.backLeft = SwerveModule(0, 0, 0, 0)
        self.backRight = SwerveModule(0, 0, 0, 0)

        self.gyro = wpilib.AnalogGyro(0)

        self.kinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.frontLeftLocation,
            self.frontRightLocation,
            self.backLeftLocation,
            self.backRightLocation,
        )

        # turn on NetworkTables
        nt = ntcore.NetworkTableInstance.getDefault()
        topic = nt.getStructArrayTopic("/SwerveStates", SwerveModuleState)
        self.pub = topic.publish()

        self.gyro.reset()



    def drive(
        self,
        xSpeed: float,
        ySpeed: float,
        rot: float,
        fieldRelative: bool,
        periodSeconds: float,
    ) -> None:

        chassis_speeds = (
            wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                xSpeed, ySpeed, rot, self.gyro.getRotation2d()
            )
            if fieldRelative
            else wpimath.kinematics.ChassisSpeeds(xSpeed, ySpeed, rot)
        )

        discretized_speeds = wpimath.kinematics.ChassisSpeeds.discretize(
            chassis_speeds, periodSeconds
        )

        swerveModuleStates = self.kinematics.toSwerveModuleStates(discretized_speeds)
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, kMaxSpeed
        )

        self.frontLeft.setDesiredState(swerveModuleStates[0])
        self.frontRight.setDesiredState(swerveModuleStates[1])
        self.backLeft.setDesiredState(swerveModuleStates[2])
        self.backRight.setDesiredState(swerveModuleStates[3])

        # make sim ting see
        self.pub.set(swerveModuleStates)
