"""
  Written by Younsung Lee on Jul. 21. 2021.
  BOJ 11653 "소인수분해"
"""

n = int(input())

# n이 1인 경우 아무것도 출력하지 않음
while n != 1:
	for i in range(2, n + 1):
		if n % i == 0:
			n = n // i
			print(i)
			break
