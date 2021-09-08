"""
    Author  : Younsung Lee
    Date    : 2021-09-09
    Site    : BOJ
    Pr Num  : 2921
    Pr Info : 도미노
"""

n = int(input())
sum = 0
for i in range(0, n + 1):
    for j in range(i, n + 1):
        sum += i + j
print(sum)
