"""
    Author  : Younsung Lee
    Date    : 9/4/2021
    Site    : BOJ
    Pr Num  : 2576
    Pr Info : 홀수
"""

nums = []

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        nums.append(n)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)