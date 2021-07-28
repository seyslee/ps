"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 11367 "Report Card Time"
"""

case = int(input())

for _ in range(case):
	name, score = input().split()
	score = int(score)
	gpa = ""

	if score >= 97:
		gpa = "A+"
	elif score >= 90:
		gpa = "A"
	elif score >= 87:
		gpa = "B+"
	elif score >= 80:
		gpa = "B"
	elif score >= 77:
		gpa = "C+"
	elif score >= 70:
		gpa = "C"
	elif score >= 67:
		gpa = "D+"
	elif score >= 60:
		gpa = "D"
	else:
		gpa = "F"
	print(name, gpa)
