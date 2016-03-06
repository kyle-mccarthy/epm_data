import pandas as pd
import numpy as np 
import math as m

df = pd.read_csv('clean_joined_grade_data.csv')
sLength = len(df['ex_2_total'])
outputDf = df.copy(deep=True)
outputGrades = []
averageExamScore = []
letterGrades = []

for index, row in outputDf.iterrows():
    # Variables
    sessionsAttended = 0
    averageIntermediateGrade = 0
    examsTaken = 0
    averageExamGrade = 0

    # Algorithm for session grades 
    intermediateSessions = ['intermediate_session_2', 'intermediate_session_3', 'intermediate_session_4', 'intermediate_session_5', 'intermediate_session_6']
    for session in intermediateSessions:
        if row[session] == 0:
            continue
        else:
            sessionsAttended = sessionsAttended + 1
            averageIntermediateGrade = averageIntermediateGrade + row[session]
    if sessionsAttended != 0:
        outputGrades.append(float(averageIntermediateGrade/sessionsAttended))
    else:
        outputGrades.append(None)

    examList = ['ex_1_total', 'ex_2_total']
    for exam in examList:
        if m.isnan(row[exam]):
            continue
        else:
            examsTaken = examsTaken + 1
            averageExamGrade = averageExamGrade + row[exam]
    if examsTaken != 0:
        averageGrade = float(averageExamGrade/examsTaken)
        averageExamScore.append(averageGrade)
        if (averageGrade > 90):
            letterGrades.append("A")
        elif (averageGrade > 80):
            letterGrades.append("B")
        elif (averageGrade > 70):
            letterGrades.append("C")
        elif (averageGrade > 60):
            letterGrades.append("D")
        else:
            letterGrades.append("F")
    else:
        averageExamScore.append(None)
        letterGrades.append(None)


outputDf['letterGrade'] = letterGrades
outputDf['averageIntermediateScore'] = outputGrades
outputDf['averageExamScore'] = averageExamScore
for index, row in outputDf.iterrows():
    print(index, row['averageIntermediateScore'], row['averageExamScore'])

outputDf.to_csv('average_exam_grades_by_intermediate_scores.csv')