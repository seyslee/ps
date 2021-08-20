"""
  Written by Younsung Lee on Aug. 20. 2021.
  BOJ 2444 "별 찍기 - 7"
"""

n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(1, n):
    print(" " * i + "*" * (2 * (n - i) - 1))