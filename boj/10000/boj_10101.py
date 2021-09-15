"""
    Author  : Younsung Lee
    Date    : 2021-09-16
    Site    : BOJ
    Pr Num  : 10101
    Pr Info : 삼각형 외우기
"""

angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
	if angle[0] == angle[1] == angle[2]:
		print("Equilateral")
	elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
		print("Isosceles")
	else:
		print("Scalene")
else:
	print("Error")
