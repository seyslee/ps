"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 4101 "Which is greater?"
"""

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a > b:
        print("Yes")
    else:
        print("No")
