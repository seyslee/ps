"""
    Author  : Younsung Lee
    Date    : 2021-09-24
    Site    : BOJ
    Pr Num  : 2750
    Pr Info : 수 정렬하기
"""

c = int(input())
numbers = []

for _ in range(c):
	numbers.append(int(input()))
numbers = sorted(numbers)

for x in numbers:
	print(x)
