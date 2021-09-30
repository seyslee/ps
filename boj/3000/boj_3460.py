"""
    Author  : Younsung Lee
    Date    : 2021-09-30
    Site    : BOJ
    Pr Num  : 3460
    Pr Info : 이진수
"""

c = int(input())

for _ in range(c):
	n = bin(int(input()))[2:]
	for i in range(len(n)):
		if n[(-i) - 1] == '1':
			print(i, end=' ')
