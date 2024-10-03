# Qns.3
# WITU has tasked you to automate a simple grading system.
# As a python student, write a program using to display the grades that the student will be reciving based on the marks scored in a subject.
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is B
# 70% - 79%   Grade is C
# 60% - 69%   Grade is D
# 50% - 59%   Grade is E
# < 50% Fail

#soln.
score = int(input('Enter the students score: \t'))

if 90 <= score <= 100:
    print('Grade is A')
elif 80 <= score <= 89:
    print('Grade is B')  
elif 70 <= score <= 69:
    print('Grade is C')
elif 60 <= score <= 69:
    print('Grade is D')
elif 50 <= score <= 59:
    print('Grade is E')
else:
    print('fail')            

