"""
    Author  : Younsung Lee
    Date    : 2021-09-27
    Site    : BOJ
    Pr Num  : 1357
    Pr Info : 뒤집힌 덧셈
"""

x, y = map(str, input().split())
total = str(int(x[::-1]) + int(y[::-1]))
print(int(total[::-1]))
