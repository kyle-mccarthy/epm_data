from Session import Session


class Student:

    def __init__(self, student_id):
        self.id = student_id
        self.sessions = {}
        self.intermediate_grades = {}
        self.final_exams = {}

    # calculate the mean for the intermediate session values, there are 5 sessions that are graded so we can just sum
    # scores and then divide by 5
    def get_mean_intermediate(self):
        total_score = 0
        for session, score in self.intermediate_grades.items():
            total_score += score
        return total_score/5

    # quick getter for accessing the exam 1 score, if the student didn't take the exam the value -1 will be returned
    def get_ex_1_score(self):
        if 1 in self.final_exams:
            return self.final_exams[1].total
        return -1

    # quick getter for accessing the exam 2 score, if the student didn't take the exam the value -1 will be returned
    def get_ex_2_score(self):
        if 2 in self.final_exams:
            return self.final_exams[2].total
        return -1

    # quick getter for accessing the best of the exam scores, if the value -1 is returned that indicates that their
    # first and second exam scores were both non existent indicating that they did not finish the class
    def get_best_final_score(self):
        ex_1 = self.get_ex_1_score()
        ex_2 = self.get_ex_2_score()
        if ex_1 > ex_2:
            return ex_1
        return ex_2

    # get the letter grade for the best final exam score
    def get_best_exam_letter(self):
        score = self.get_best_final_score()
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
