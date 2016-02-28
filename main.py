from Parser import Parser
import time

p = Parser()
p.load()
print(p.students[1].sessions[2].grade)