"""
    Author  : Younsung Lee
    Date    : 2021-09-10
    Site    : BOJ
    Pr Num  : 2581
    Pr Info : 소수
"""

m = int(input())
n = int(input())
primes = []

for i in range(m, n + 1):
	count = 0
	for j in range(1, i + 1):
		if i % j == 0:
			count += 1
			if count > 2:
				break
	if count == 2:
		primes.append(i)

if len(primes) != 0:
	print(sum(primes))
	print(primes[0])
else:
	print(-1)
