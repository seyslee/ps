"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 8393 "합"
"""

n = int(input())
sum = 0

for i in range(n, 0, -1):
	sum += i
print(sum)
