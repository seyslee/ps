"""
    Author  : Younsung Lee
    Date    : 2021-09-16
    Site    : BOJ
    Pr Num  : 2711
    Pr Info : 오타맨 고창영
"""

c = int(input())

for _ in range(c):
	i, s = input().split()
	i = int(i)
	print(s[:i-1], s[i:], sep='')
