#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

#Input Format:
#The first line contains the integer n, the number of students' records. 
#The next n lines contain the names and marks obtained by a student, each value separated by a space. 
#The final line contains query_name, the name of a student to query.


def avgMarks():
  n = int(input())
  student_marks = {}

  for _ in range(n):
    name, *line = input().split()
    scores = list (map(float, line))
    student_marks[name] = scores
  stdnt_name = input()

  marks = student_marks[stdnt_name]
  avg_mark = sum(marks)/len(marks)
  print(f"{avg_mark:.2f}")

avgMarks()