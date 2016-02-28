from Session import Session


class Student:

    def __init__(self, student_id):
        self.id = student_id
        self.sessions = {}
        self.intermediate_grades = {}
        self.final_exams = {}