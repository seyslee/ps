"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 10156 "과자"
"""

k, n, m = map(int, input().split())
money = k * n - m

if money > 0:
	print(money)
elif money < 0:
	money = 0
	print(money)
else:
	print(money)
