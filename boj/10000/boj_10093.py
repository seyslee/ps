"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 10093 "Numbers"
"""

a, b = map(int, input().split())
s = min(a, b)
l = max(a, b)
n = l - s - 1

if s == l or s + 1 == l:
	n = 0
print(n)

for i in range(s+1, l):
	print(i, end=" ")
