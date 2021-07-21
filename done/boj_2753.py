"""
  Written by Younsung Lee on Jul. 21. 2021.
  BOJ 2753 "윤년"
"""

year = int(input())

if year % 4 == 0:
	if year % 100 != 0:
		print(1)
	elif year % 400 == 0:
		print(1)
	else:
		print(0)
else:
	print(0)
