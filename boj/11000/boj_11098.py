"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 11098 "첼시를 도와줘!"
"""

n = int(input())

for _ in range(n):
    p = int(input())
    max_price = 0
    max_name = ""
    for _ in range(p):
        c, n = input().split()
        c = int(c)
        if max_price < c:
            max_price = c
            max_name = n
    print(max_name)
