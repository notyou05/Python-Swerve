import time

class SwervePhysicsEngine:
    def __init__(self, StartX, StartY, StartRotation, accelerationXY, accelerationRot, decelerationXY, decelerationRot):
        self.StartX = StartX
        self.StartY = StartY
        self.StartRotation = StartRotation  # in degrees
        self.accelerationXY = accelerationXY  # m/s²
        self.accelerationRot = accelerationRot  # deg/s²
        self.decelerationXY = decelerationXY  # m/s²
        self.decelerationRot = decelerationRot  # deg/s²

        # Initialize the current state variables
        self.CurentX = StartX
        self.CurentY = StartY
        self.CurentRotation = StartRotation

    def update(self, X, Y, Rotation):
        # Update the position and rotation over time, assuming delta time is fixed at 0.01s

        self.CurentX += X / 0.1
        self.CurentY += Y / 0.1
        self.CurentRotation += Rotation / 0.1

    def get_state(self):
        # Return the current state (X, Y, Rotation)
        return self.CurentX, self.CurentY, self.CurentRotation

# Example instantiation
robot = SwervePhysicsEngine(0, 0, 0, 1, 1, 1, 1)

# Run the update loop for a specific number of iterations
for _ in range(10):  # Example: Run for 10 iterations
    # Example update call
    robot.update(1, 1, 0)

    # Print the current state
    print(robot.get_state())
    time.sleep(0.01)  # Simulate time delay for the next update
