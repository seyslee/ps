"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 2439 "별 찍기 - 2"
"""

n = int(input())

for x in range(1, n+1):
    print(' ' * (n -x) + '*' * x)
