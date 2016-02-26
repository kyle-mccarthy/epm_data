from Session import Session
from Student import Student
from os import listdir


class Parser:

    def __init__(self):
        self.path = "sessions/"
        self.num_session = 6
        self.students = {}
        self.init_students()

    # initialize the list of students
    def init_students(self):
        for i in range(1, 116):
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
            row = row.split(',')
            # get the needed variables from the row
            session_id = int(row[0].lstrip().rstrip())
            student_id = int(row[1].lstrip().rstrip())
            exercise = row[2].lstrip().rstrip()
            activity = row[3].lstrip().rstrip()
            start_time = row[4].lstrip().rstrip()
            end_time = row[5].lstrip().rstrip()
            idle_time = row[6].lstrip().rstrip()
            mouse_wheel = row[7].lstrip().rstrip()
            mouse_wheel_click = row[8].lstrip().rstrip()
            mouse_click_left = row[9].lstrip().rstrip()
            mouse_click_right = row[10].lstrip().rstrip()
            mouse_movement = row[11].lstrip().rstrip()
            keystroke = row[12].lstrip().rstrip()

            # create the session
            session = Session(session_id, exercise, activity, start_time, end_time, idle_time, mouse_wheel,
                              mouse_wheel_click, mouse_click_left, mouse_click_right, mouse_movement, keystroke)

            # attach the session to the student
            self.students[student_id].sessions[session_id] = session
