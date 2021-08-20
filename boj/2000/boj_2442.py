"""
  Written by Younsung Lee on Aug. 18. 2021.
  BOJ 2442 "별 찍기 - 5"
"""

n = int(input())

for i in range(1, n + 1):
    b = ' ' * (n - i) + '*' * ((2 * i) - 1)
    print(b)
