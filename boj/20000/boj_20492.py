"""
  Written by Younsung Lee on Aug. 4. 2021.
  BOJ 20492 "세금"
"""

n = int(input())
r1 = int(n - (n * 0.22))
r2 = int(n - (n - n * 0.8) * 0.22)
print(r1, r2)
