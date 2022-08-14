#Given the names and grades for each student in a class of  students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, 
#order their names alphabetically and print each name on a new line.

no_of_stdnts = int(input())
scores = [[input(), float(input())] for _ in range(no_of_stdnts)]
second_lowest = sorted(list(set([score for name, score in scores])))[1]
print('\n'.join([s_lowest for s_lowest,s_lowest2 in sorted(scores) if s_lowest2 == second_lowest]))