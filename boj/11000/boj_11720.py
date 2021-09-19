"""
    Author  : Younsung Lee
    Date    : 2021-09-19
    Site    : BOJ
    Pr Num  : 11720
    Pr Info : 숫자의 합
"""

n = int(input())
z = str(input())
total = 0
for i in range(0, n):
    total += int(z[i])
print(total)