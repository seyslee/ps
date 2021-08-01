"""
  Written by Younsung Lee on Aug. 1. 2021.
  BOJ 17009 "Winning Score"
"""

li_a = [int(input()) for _ in range(3)]
li_b = [int(input()) for _ in range(3)]
a = li_a[0] * 3 + li_a[1] * 2 + li_a[2]
b = li_b[0] * 3 + li_b[1] * 2 + li_b[2]

if a == b:
    print("T")
elif a > b:
    print("A")
else:
    print("B")
