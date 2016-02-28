from Session import Session
from Student import Student
from Exam import Exam
from os import listdir
import time
import pandas as pd
import statistics


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
        for s in range(1, self.num_session+1):
            # iterate files
            for f in listdir(self.path + str(s)):
                self.parse_session_file(s, f)
        self.parse_intermediate_grades()
        self.parse_final_grades()

    # parse the file and extract the data needed from it, then create the session and attach it to the correct user
    def parse_session_file(self, session, file_name):
        file = open(self.path + str(session) + "/" + str(file_name))
        for row in file:
            row = row.split(',')
            # get the needed variables from the row and trim the string and perform type conversions
            session_id = int(row[0].lstrip().rstrip())
            student_id = int(row[1].lstrip().rstrip())
            exercise = row[2].lstrip().rstrip()
            activity = row[3].lstrip().rstrip()

            # convert the string dates to actual dates
            start_time = row[4].lstrip().rstrip()
            end_time = row[5].lstrip().rstrip()

            # catch the possibility that the data is malformatted
            try:
                time.strptime(start_time, "%d.%m.%Y %H:%M:%S")
            except ValueError:
                print("error converting str to time for session " + str(session_id) + " in file " + file_name +
                      " for the date " + start_time)

            # catch the possibility that the data is malformatted
            try:
                time.strptime(end_time, "%d.%m.%Y %H:%M:%S")
            except ValueError:
                print("error converting str to time for session " + str(session_id) + " in file " + file_name +
                      " for the date " + end_time)

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

    # parse the intermediate grades
    def parse_intermediate_grades(self):
        # open the intermediate grades file using pandas
        f = pd.read_excel('grades/intermediate_grades.xlsx', index_col=None, na_values=['NA'])
        for index, row in f.iterrows():
            student_id = int(row[0])
            # set the intermediate grades for the sessions 2-6 from the intermediate grades file
            for i in range(1, 6):
                self.students[student_id].intermediate_grades[i+1] = row[i]

    # parse the final grade information and save it for the student
    def parse_final_grades(self):
        # there are two pages in the workbook we need to look at the first one is the first exam,
        # and the second page is the second exam
        for ex_num in range(0, 2):
            ex = pd.read_excel('grades/final_grades.xlsx', ex_num, index_col=None, na_values=['NA'])
            for index, row in ex.iterrows():
                student_id = int(row[0])
                # this isn't the cleanest way but what it does is pick the value from the row/col and then it maps it
                # to the object, there isn't really any reason to assign each row to a variable and then pass it to the
                # constructor other than readibility, but its a lot to type
                exam = Exam(ex_num, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                            row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                self.students[student_id].final_exams[ex_num+1] = exam

    # get a list of all the intermediate grades from the sessions from the students
    def get_list_session_scores(self):
        # initialize the session score container
        session_scores = {2: [], 3: [], 4: [], 5: [], 6: []}
        for student_id, student in self.students.items():
            for session, score in student.intermediate_grades.items():
                session_scores[session].append(score)
        return session_scores

    # get the average of the session scores/intermediate grades
    def get_average_session_scores(self):
        session_averages = {}
        for session_id, grades in self.get_list_session_scores().items():
            session_averages[session_id] = statistics.mean(grades)
        return session_averages

    # get the median of the session scores/intermediate grades
    def get_median_session_scores(self):
        session_medians = {}
        for session_id, grades in self.get_list_session_scores().items():
            session_medians[session_id] = statistics.median(grades)
        return session_medians

