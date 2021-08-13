"""
  Written by Younsung Lee on Aug. 13. 2021.
  BOJ 2441 "별 찍기 - 4"
"""

n = int(input())

for x in range(n, 0, -1):
    print(" " * (n - x) + "*" * x)
