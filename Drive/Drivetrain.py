import math
import wpilib
import wpimath.geometry
import wpimath.kinematics
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
import Drive.SwervePhysicsEngine
import Drive.SwerveModule
import ntcore
from wpimath.kinematics import SwerveModuleState

kMaxSpeed = 3.0  # 3 meters per second
kMaxAngularSpeed = math.pi  # 1/2 rotation per second


class Drivetrain:
    """
    Represents a swerve drive style drivetrain.
    """

    def __init__(self) -> None:
        self.frontLeftLocation = wpimath.geometry.Translation2d(0.381, 0.381)
        self.frontRightLocation = wpimath.geometry.Translation2d(0.381, -0.381)
        self.backLeftLocation = wpimath.geometry.Translation2d(-0.381, 0.381)
        self.backRightLocation = wpimath.geometry.Translation2d(-0.381, -0.381)

        # Initialize SwerveModules with correct port IDs for your hardware
        self.frontLeft = Drive.SwerveModule.SwerveModule(1, 2, 0, 1)
        self.frontRight = Drive.SwerveModule.SwerveModule(3, 4, 4, 5)
        self.backLeft = Drive.SwerveModule.SwerveModule(5, 6, 8, 9)
        self.backRight = Drive.SwerveModule.SwerveModule(7, 8, 12, 13)

        self.gyro = wpilib.AnalogGyro(0)

        self.kinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.frontLeftLocation,
            self.frontRightLocation,
            self.backLeftLocation,
            self.backRightLocation,
        )

        self.gyro.reset()

        nt = ntcore.NetworkTableInstance.getDefault()
        # Start publishing an array of module states with the "/SwerveStates" key
        topic = nt.getStructArrayTopic("/SwerveStates", SwerveModuleState)
        topic2 = nt.getStructArrayTopic("/Pose2D", Pose2d)
        self.pub = topic.publish()
        self.pub2 = topic2.publish()

    def drive(
        self,
        xSpeed: float,
        ySpeed: float,
        rot: float,
        fieldRelative: bool,
        periodSeconds: float,
    ) -> None:
        """
        Method to drive the robot using joystick info.
        :param xSpeed: Speed of the robot in the x direction (forward).
        :param ySpeed: Speed of the robot in the y direction (sideways).
        :param rot: Angular rate of the robot.
        :param fieldRelative: Whether the provided x and y speeds are relative to the field.
        :param periodSeconds: Time
        """
        swerveModuleStates = self.kinematics.toSwerveModuleStates(
            wpimath.kinematics.ChassisSpeeds.discretize(
                (
                    wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                        xSpeed, ySpeed, rot, self.gyro.getRotation2d()
                    )
                    if fieldRelative
                    else wpimath.kinematics.ChassisSpeeds(xSpeed, ySpeed, rot)
                ),
                periodSeconds,
            )
        )
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, kMaxSpeed
        )
        self.frontLeft.setDesiredState(swerveModuleStates[0])
        self.frontRight.setDesiredState(swerveModuleStates[1])
        self.backLeft.setDesiredState(swerveModuleStates[2])
        self.backRight.setDesiredState(swerveModuleStates[3])

        self.pub.set([swerveModuleStates[0], swerveModuleStates[1], swerveModuleStates[2], swerveModuleStates[3]])  # Publish the states to the network table

        # Assuming the update method does not require self as a parameter
        swerve_engine = Drive.SwervePhysicsEngine.SwervePhysicsEngine(0, 0, 0, 1, 1, 1, 1)
        swerve_engine.update(xSpeed, ySpeed, rot)

        # Getting the current state after update
        current_state = swerve_engine.get_state()

        # Assuming current_state is a tuple with X, Y, Rotation in that order
        pose = Pose2d(current_state[0], current_state[1], Rotation2d.fromDegrees(current_state[2]))
        self.pub2.set([pose])  # Publish the pose to the network table

