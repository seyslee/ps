"""
  Written by Younsung Lee on Aug. 21. 2021.
  BOJ 2446 "별 찍기 - 9"
"""

n = int(input())

for i in range(0, n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(n - 2, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))