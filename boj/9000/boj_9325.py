"""
  Written by Younsung Lee on Aug. 20. 2021.
  BOJ 9325 "얼마?"
"""

n = int(input())

for _ in range(n):
    total = 0
    s = int(input())
    m = int(input())
    if m != 0:
        for _ in range(m):
            q, p = map(int, input().split())
            total += (q * p)
    total += s
    print(total)

