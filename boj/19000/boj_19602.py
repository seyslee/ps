"""
  Written by Younsung Lee on Aug. 4. 2021.
  BOJ 19602 "Dog Treats"
"""

s = int(input())
m = int(input())
l = int(input())

happiness = 1 * s + 2 * m + 3 * l
if happiness >= 10:
	print("happy")
else:
	print("sad")
