"""
  Written by Younsung Lee on Aug. 21. 2021.
  BOJ 9295 "Dice"
"""

t = int(input())

for i in range(1, t +1):
    a, b = map(int, input().split())
    print("Case %d: %d" % (i, a + b))