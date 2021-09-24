"""
    Author  : Younsung Lee
    Date    : 2021-09-24
    Site    : BOJ
    Pr Num  : 2577
    Pr Info : 숫자의 개수
"""

a = int(input())
b = int(input())
c = int(input())

total = list(str(a * b * c))
for i in range(10):
	print(total.count(str(i)))
