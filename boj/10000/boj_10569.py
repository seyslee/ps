"""
  Written by Younsung Lee on Aug. 26. 2021.
  BOJ 10569 "Polyhedra"
"""

n = int(input())

for _ in range(n):
	v, e = map(int, input().split())
	s = 2 - v + e
	print(s)
