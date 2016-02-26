from Session import Session
from Student import Student
from os import listdir


class Parser:

    def __init__(self):
        self.path = "sessions/"
        self.num_session = 6
        self.students = []
        self.init_students()

    # initialize the list of students
    def init_students(self):
        for i in range(1, 115):
            self.students[i] = Student(i)

    # iterate through the sessions file and each session folder and then get the files in the session folder
    # the iterate the files in the session folder
    def load(self):
        # iterate folders
        for s in range(1, self.num_session):
            # iterate files
            for f in listdir(self.path + str(s)):
                self.parse_file(s, f)

    # parse the file and extract the data needed from it, then create the session and attach it to the correct user
    def parse_file(self, session, file_name):
        file = open(self.path + str(session) + "/" + str(file_name))
        for row in file:
            # get the needed variables from the row
            session_id = row[0]
            student_id = row[1]
            exercise = row[2]
            activity = row[3]
            start_time = row[4]
            end_time = row[5]
            idle_time = row[6]
            mouse_wheel = row[7]
            mouse_wheel_click = row[8]
            mouse_click_left = row[9]
            mouse_click_right = row[10]
            mouse_movement = row[11]
            keystroke = row[12]

            # create the session
            session = Session(session_id, exercise, activity, start_time, end_time, idle_time, mouse_wheel,
                              mouse_wheel_click, mouse_click_left, mouse_click_right, mouse_movement, keystroke)

            # attach the session to the student
            self.students[student_id].session[session_id] = session
