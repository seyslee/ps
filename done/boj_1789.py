"""
  Written by Younsung Lee on Jul. 26. 2021.
  BOJ 1789 "수들의 합"
"""

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
