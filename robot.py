import wpilib
from Drive.Drivetrain import Drivetrain

class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        """Initialize robot components."""
        self.drivetrain = Drivetrain()
        self.driverController = wpilib.XboxController(0)
    def teleopPeriodic(self) -> None:
        """Drive with joystick during teleop."""
        self.drivetrain.drive(self.driverController.getLeftY(), self.driverController.getLeftX(), self.driverController.getRightX(), fieldRelative=False, periodSeconds=self.getPeriod())

    def simulationPeriodic(self):
        """Updates simulation physics."""
        self.drivetrain.simulationPeriodic()


if __name__ == "__main__":
    wpilib.run(MyRobot)
