from Parser import Parser

p = Parser()
p.load()

# get the intermediate averages
intm_averages = p.get_average_session_scores()
print("intermediate averages: " + str(intm_averages))

# get the intermediate medians
intm_medians = p.get_median_session_scores()
print("intermediate medians: " + str(intm_medians))

# get the intermediate modes
intm_modes = p.get_mode_session_scores()
print("intermediate modes: " + str(intm_modes))

# get the intermediate standard deviations
intm_std_devs = p.get_std_dev_session_scores()
print("intermediate std_devs: " + str(intm_std_devs))

# get the exam score averages
exam_averages = p.get_average_exam_scores()
print("exam averages: " + str(exam_averages))

# get the exam score medians
exam_medians = p.get_median_exam_scores()
print("exam medians: " + str(exam_medians))

# get the exam score mode
exam_modes = p.get_mode_exam_scores()
print("exam modes: " + str(exam_modes))

# get the exam score std deviations
exam_std_dev = p.get_std_dev_exam_scores()
print("exam std dev: " + str(exam_std_dev))

# export the joined session and intermediate grade data to a CSV
p.export_joined_session_grade_data()
