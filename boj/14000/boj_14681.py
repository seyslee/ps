"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 14681 "Quadrant Selection"
"""

x = int(input())
y = int(input())

if x > 0 and y > 0:
	print(1)
elif x < 0 and y > 0:
	print(2)
elif x < 0 and y < 0:
	print(3)
elif x > 0 and y < 0:
	print(4)
