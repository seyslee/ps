"""
  Written by Younsung Lee on Aug. 20. 2021.
  BOJ 2010 "플러그"
"""

import sys

n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    total += int(sys.stdin.readline())
print(total - (n - 1))
