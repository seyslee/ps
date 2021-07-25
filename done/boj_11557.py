"""
  Written by Younsung Lee on Jul. 25. 2021.
  BOJ 11557 "Yangjojang of The Year"
"""

case = int(input())

for _ in range(case):
    n = int(input())
    max_alcohol = 0
    dic = {}

    for _ in range(n):
        univ, alcohol = input().split()
        dic[alcohol] = univ

    for x in dic.keys():
        if int(max_alcohol) < int(x):
            max_alcohol = x

    print(dic[max_alcohol])
