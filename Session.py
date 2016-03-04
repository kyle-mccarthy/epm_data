import time


class Session:

    def __init__(self, session_id):
        self.session_id = session_id
        self.intermediate_grade = None
        self.activities = []


class Activity:

    def __init__(self, session_id, exercise, activity, start_time, end_time, idle_time, mouse_wheel, mouse_wheel_click,
                 mouse_click_left, mouse_click_right, mouse_movement, keystroke):
        self.session_id = session_id
        self.exercise = exercise
        self.activity = activity
        self.start_time = start_time
        self.end_time = end_time
        self.idle_time = idle_time
        self.mouse_wheel = mouse_wheel
        self.mouse_wheel_click = mouse_wheel_click
        self.mouse_click_left = mouse_click_left
        self.mouse_click_right = mouse_click_right
        self.mouse_movement = mouse_movement
        self.keystroke = keystroke
        self.elapsed_time = None
        self.clean()

    def clean(self):
        self.start_time = time.mktime(self.start_time)
        self.end_time = time.mktime(self.end_time)
        if int(self.idle_time) < 0:
            self.idle_time = 0
        if self.start_time is not None and self.end_time is not None:
            self.elapsed_time = self.end_time - self.start_time

    def to_dict(self):
        return {
            'session_id': self.session_id,
            'exercise': self.exercise,
            'activity': self.activity,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'idle_time': self.idle_time,
            'mouse_wheel': self.mouse_wheel,
            'mouse_wheel_click': self.mouse_wheel_click,
            'mouse_click_left': self.mouse_click_left,
            'mouse_click_right': self.mouse_click_right,
            'mouse_movement': self.mouse_movement,
            'keystroke': self.keystroke,
            'elapsed_time': self.elapsed_time
        }
