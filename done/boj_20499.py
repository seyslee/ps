"""
  Written by Younsung Lee on Aug. 9. 2021.
  BOJ 20499 "Darius님 한타 안 함?"
"""

k, d, a = map(int, input().split('/'))

if k + a < d or d == 0:
	print("hasu")
else:
	print("gosu")
