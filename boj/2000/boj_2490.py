"""
    Author  : Younsung Lee
    Date    : 2021-09-06
    Site    : BOJ
    Pr Num  : 2490
    Pr Info : 윷놀이
"""

for _ in range(3):
	yuts = list(map(int, input().split()))
	if yuts.count(0) == 1:
		print("A")
	elif yuts.count(0) == 2:
		print("B")
	elif yuts.count(0) == 3:
		print("C")
	elif yuts.count(0) == 4:
		print("D")
	else:
		print("E")
