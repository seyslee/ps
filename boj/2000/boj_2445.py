"""
  Written by Younsung Lee on Aug. 20. 2021.
  BOJ 2445 "별 찍기 - 8"
"""

n = int(input())

for i in range(1, n + 1):
    print("*" * i + " " * (n * 2 - i * 2) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (n - i) * 2 + "*" * i)