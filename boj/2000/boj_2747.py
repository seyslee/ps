"""
    Author  : Younsung Lee
    Date    : 2021-09-07
    Site    : BOJ
    Pr Num  : 2747
    Pr Info : 피보나치 수
"""

n = int(input())
nums = [0, 1]
for _ in range(2, n + 1):
	nums.append(nums[-1] + nums[-2])
print(nums[n])
