"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 3052
    Pr Info : 나머지
"""

nums = []
for _ in range(10):
	n = int(input())
	nums.append(n % 42)
nums = set(nums)
print(len(nums))
