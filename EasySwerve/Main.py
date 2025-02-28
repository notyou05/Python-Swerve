
class easyswerve:
    def __init__(self, max_speed: float, max_turn_speed: float, max_acceleration: float, encoderoffset: float): #add encoder offset for all modules
        self.max_speed = max_speed
        self.max_acceleration = max_acceleration
        self.max_turn_speed = max_turn_speed
        self.encoderoffset = encoderoffset
    """make wheel spin less far"""
    def wheel_optimization(self, target_wheel_angle: float, encoder_value: float):  # encoder value = real encoder value - offset

        if encoder_value - target_wheel_angle > 90:
            optimized_wheel_angle = target_wheel_angle - 180  # might chave to chage - to +
            is_inverted = True  # might need to chage
        else:
            optimized_wheel_angle = target_wheel_angle
            is_inverted = False  # might need to chage

        return optimized_wheel_angle, is_inverted

    """sets drive mode"""
    def joystick_input(self, left_joystick_x, left_joystick_y, right_joystick_x):
        robot_centric_angle_to_drive = atan2(left_joystick_y, left_joystick_x)
        robot_centric_speed_to_drive = math.sqrt(left_joystick_x**2 + left_joystick_y**2) * self.max_speed #add acselration constant later
        rotation_to_drive = right_joystick_x * self.max_turn_speed

        if right_joystick_x == 0 and left_joystick_x != 0 and left_joystick_y != 0:
            mode = "drive"
        elif right_joystick_x != 0 and left_joystick_x != 0 and left_joystick_y != 0:
            mode = "drive and turn"
        elif right_joystick_x != 0 and left_joystick_x == 0 and left_joystick_y != 0:
            mode = "turn"
        else:
            mode = "x"
        return robot_centric_angle_to_drive, robot_centric_speed_to_drive, rotation_to_drive, mode

    """make robot smooth brain to drive"""
    def field_centric_calclator(self, robot_centric_angle_to_drive: float, gyro_angle: float):
        field_centric_angle_to_drive = robot_centric_angle_to_drive - gyro_angle # change to + idk prob not
        return field_centric_angle_to_drive


    """tell wheels what to do aka wheel whisper"""
    def set_module_state(self, angle_to_drive: float, speed_to_drive: float, mode: str):
        if mode == "drive":
            """front_left"""
            front_left_state = [speed_to_drive, angle_to_drive]
            """front_right"""
            front_right_state = [speed_to_drive, angle_to_drive]
            """back_left"""
            back_left_state = [speed_to_drive, angle_to_drive]
            """back_right"""
            back_right_state = [speed_to_drive, angle_to_drive]
        elif mode == "turn":
            """front_left"""
            front_left_state = [speed_to_drive, 45]
            """front_right"""
            front_right_state = [speed_to_drive, 135]
            """back_left"""
            back_left_state = [speed_to_drive, 225]
            """back_right"""
            back_right_state = [speed_to_drive, 315]
        elif mode == "drive and turn":
            # to do lots of math
            pass
        elif mode == "x":
            """front_left"""
            front_left_speed_out = 0
            front_left_angle_out = 45
            """front_right"""
            front_right_speed_out = 0
            front_right_angle_out = 135
            """back_left"""
            back_left_speed_out = 0
            back_left_angle_out = 225
            """back_right"""
            back_right_speed_out = 0
            back_right_angle_out = 315
        else: print("mode error")

        return front_left_speed_out, front_left_angle_out, front_right_speed_out, front_right_angle_out, back_left_speed_out, back_left_angle_out, back_right_speed_out, back_right_angle_out


