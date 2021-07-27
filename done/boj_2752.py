"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 2752 "세수정렬"
"""

nums = list(map(int, input().split()))
nums.sort()
print(nums[0], nums[1], nums[2])
