"""
    Author  : Younsung Lee
    Date    : 2021-09-07
    Site    : BOJ
    Pr Num  : 10833
    Pr Info : 사과
"""

n = int(input())
leftover = 0

for _ in range(n):
	s, a = map(int, input().split())
	leftover += a % s
print(leftover)
