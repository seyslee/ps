"""
    Author  : Younsung Lee
    Date    : 2021-09-08
    Site    : BOJ
    Pr Num  : 2501
    Pr Info : 약수 구하기
"""

n, k = map(int, input().split())
divisors = []

for i in range(1, n + 1):
	if n % i == 0:
		divisors.append(i)

if len(divisors) >= k:
	print(divisors[k - 1])
else:
	print(0)
