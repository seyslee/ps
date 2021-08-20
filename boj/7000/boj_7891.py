"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 7891 "Can you add this?"
"""

case = int(input())

for _ in range(case):
	a, b = map(int, input().split())
	print(a + b)
