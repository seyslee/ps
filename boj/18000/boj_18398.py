"""
  Written by Younsung Lee on Aug. 3. 2021.
  BOJ 18398 "HOMWRK"
"""

t = int(input())
for _ in range(t):
    case = int(input())
    for _ in range(case):
        a, b = map(int, input().split())
        print(a + b, a * b)
