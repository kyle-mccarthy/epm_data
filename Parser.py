from Session import Session
from Student import Student
from os import listdir


class Parser:

    def __init__(self):
        self.path = "sessions/"
        self.num_session = 6
        self.students = []

    # iterate through the sessions file and each session folder and then get the files in the session folder
    # the iterate the files in the session folder
    def load(self):
        # iterate folders
        for s in range(1, self.num_session):
            # iterate files
            for f in listdir(self.path + str(s)):
                file = open(self.path + str(s) + "/" + str(f))
                self.parse_file(file)

    def parse_file(self, file):
        for row in file:
            return None
