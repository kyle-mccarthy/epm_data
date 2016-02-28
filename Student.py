from Session import Session


class Student:

    def __init__(self, id):
        self.id = id
        self.sessions = {}
        self.intermediate_grades = {}
        self.final_exams = {}