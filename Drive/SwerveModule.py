from wpimath.controller import PIDController
from phoenix6 import hardware, controls


class SwerveModule:
    def __init__(self, drive_id: int, steer_id: int, encoder_id: int, encoder_offset: float):
        self.drive_id = drive_id
        self.steer_id = steer_id
        self.encoder_offset = encoder_offset

        self.cancoder = hardware.CANcoder(encoder_id)
        self.drive_motor = hardware.TalonFX(drive_id)
        self.steer_motor = hardware.TalonFX(steer_id)

        # PID Controller for steering
        self.steer_pid = PIDController(0.1, 0.0, 0.0)  # Adjust these values

        # Control object for drive motor
        self.drive_control = controls.DutyCycleOut(0)

    def set_state(self, module_state: list[float, float]):
        wheel_speed, steer_angle = module_state  # Get list values

        # Set the drive motor speed
        self.drive_motor.set(wheel_speed)

        # Get the current steering angle (extract float from StatusSignal)
        current_angle = self.cancoder.get_position().value

        # Compute PID output
        pid_output = self.steer_pid.calculate(current_angle, steer_angle)

        # Set the control output for the steering motor
        self.steer_motor.set_control(controls.DutyCycleOut(pid_output))
