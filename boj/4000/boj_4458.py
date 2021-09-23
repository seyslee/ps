"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 4458
    Pr Info : 첫 글자를 대문자로
"""

n = int(input())

for _ in range(n):
    s = str(input())
    s = s[0].upper() + s[1:]
    print(s)
