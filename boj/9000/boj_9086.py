"""
    Author  : Younsung Lee
    Date    : 2021-09-29
    Site    : BOJ
    Pr Num  : 9086
    Pr Info : 문자열
"""

n = int(input())

for _ in range(n):
	s = input()
	print(s[0] + s[-1])
