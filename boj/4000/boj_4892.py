"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 4892 "숫자 맞추기 게임"
"""

idx = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    else:
        n1 = n0 * 3
        if n1 % 2 == 0:
            n2 = n1 / 2
        else:
            n2 = (n1 + 1) / 2
        n3 = 3 * n2
        n4 = n3 / 9
    if n1 % 2 == 1:
        print("%d. odd %d" % (idx, n4))
    else:
        print("%d. even %d" % (idx, n4))
    idx += 1
