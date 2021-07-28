"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 13597 "Tri-du"
"""

a, b = map(int, input().split())

if a == b:
	print(a)
else:
	print(max(a, b))
