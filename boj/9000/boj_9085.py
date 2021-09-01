"""
  Written by Younsung Lee on Sep. 1. 2021.
  BOJ 9085 "더하기"
"""

t = int(input())
for _ in range(t):
	nums = []
	n = int(input())
	nums = sum(list(map(int, input().split())))
	print(nums)
