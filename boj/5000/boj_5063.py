"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 5063 "TGN"
"""

case = int(input())

for _ in range(case):
	r, e, c = map(int, input().split())

	if r > (e - c):
		print("do not advertise")
	elif r < (e - c):
		print("advertise")
	else:
		print("does not matter")
