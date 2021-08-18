"""
  Written by Younsung Lee on Aug. 18. 2021.
  BOJ 2443 "별 찍기 - 6"
"""

n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
