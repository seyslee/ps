"""
  Written by Younsung Lee on Aug. 20. 2021.
  BOJ 2523 "별 찍기 - 13"
"""

n = int(input())

for i in range(1, n + 1):
    print("*" * i)
for i in range(1, n):
    print("*" * (n - i))