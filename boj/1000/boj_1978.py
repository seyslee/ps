"""
    Author  : Younsung Lee
    Date    : 2021-09-13
    Site    : BOJ
    Pr Num  : 1978
    Pr Info : 소수 찾기
"""

c = int(input())
nums = list(map(int, input().split()))
prime_count = 0

for n in nums:
    count = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count == 0:
            prime_count += 1

print(prime_count)