"""
  Written by Younsung Lee on Aug. 1. 2021.
  BOJ 17010 "Time to Decompress"
"""

case = int(input())

for _ in range(case):
    n, w = input().split()
    print(str(w) * int(n))
