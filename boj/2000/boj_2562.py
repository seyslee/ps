"""
  Written by Younsung Lee on Sep. 2. 2021.
  BOJ 2562 "최댓값"
"""

nums = []
for _ in range(9):
	nums.append(int(input()))
print(max(nums))
print(nums.index(max(nums)) + 1)
