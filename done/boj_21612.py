"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 21612 "Boiling Water"
"""

b = int(input())
p = 5 * b - 400

print(p)

if p > 100:
    print(-1)
elif p < 100:
    print(1)
else:
    print(0)
