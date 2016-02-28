from Parser import Parser

p = Parser()
p.load()
averages = p.get_average_session_scores()
print(averages)
medians = p.get_median_session_scores()
print(medians)
