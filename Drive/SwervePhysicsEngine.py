import time


class SwervePhysicsEngine:
    def __init__(self, StartX, StartY, StartRotation, accelerationXY, accelerationRot, decelerationXY, decelerationRot):
        self.StartX = StartX
        self.StartY = StartY
        self.StartRotation = StartRotation
        self.accelerationXY = accelerationXY  # m/s²
        self.accelerationRot = accelerationRot  # rad/s²
        self.decelerationXY = decelerationXY  # m/s²
        self.decelerationRot = decelerationRot  # rad/s²

        # Initialize velocities
        self.velocityX = 0  # m/s
        self.velocityY = 0  # m/s
        self.velocityRot = 0  # rad/s

        self.previous_time = time.time()

    def update(self, targetX, targetY, targetRotation):
        current_time = time.time()
        delta_time = current_time - self.previous_time

        # Update X and Y velocities based on acceleration/deceleration
        distanceX = targetX - self.StartX
        distanceY = targetY - self.StartY
        target_velocityXY = (distanceX, distanceY)

        # Apply acceleration or deceleration based on distance to target
        if abs(target_velocityXY[0]) > abs(self.velocityX):
            self.velocityX += self.accelerationXY * delta_time  # m/s² * s = m/s
        elif abs(target_velocityXY[0]) < abs(self.velocityX):
            self.velocityX -= self.decelerationXY * delta_time  # m/s² * s = m/s

        if abs(target_velocityXY[1]) > abs(self.velocityY):
            self.velocityY += self.accelerationXY * delta_time  # m/s² * s = m/s
        elif abs(target_velocityXY[1]) < abs(self.velocityY):
            self.velocityY -= self.decelerationXY * delta_time  # m/s² * s = m/s

        # Update rotation velocity based on acceleration or deceleration
        rotation_diff = targetRotation - self.StartRotation
        if abs(rotation_diff) > abs(self.velocityRot):
            self.velocityRot += self.accelerationRot * delta_time  # rad/s² * s = rad/s
        elif abs(rotation_diff) < abs(self.velocityRot):
            self.velocityRot -= self.decelerationRot * delta_time  # rad/s² * s = rad/s

        # Apply velocities to positions
        self.StartX += self.velocityX * delta_time  # m/s * s = meters
        self.StartY += self.velocityY * delta_time  # m/s * s = meters
        self.StartRotation = (self.StartRotation + self.velocityRot * delta_time) % 360  # rad/s * s = radians

        self.previous_time = current_time

    def get_state(self):
        return (self.StartX, self.StartY, self.StartRotation)
