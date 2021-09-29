"""
    Author  : Younsung Lee
    Date    : 2021-09-30
    Site    : BOJ
    Pr Num  : 11170
    Pr Info : 0의 개수
"""

c = int(input())

for _ in range(c):
	a, b = map(int, input().split())
	count = 0
	for i in range(a, b + 1):
		num = str(i)
		count += num.count('0')
	print(count)
