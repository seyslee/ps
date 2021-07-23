"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 5086 "Factors And Multiples"
"""

while True:
	a, b = map(int, input().split())

	if a == 0 and b == 0:
		break
	elif b % a == 0:
		print("factor")
	elif a % b == 0:
		print("multiple")
	else:
		print("neither")
