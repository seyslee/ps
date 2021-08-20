"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 11549 "Identifying tea"
"""

tea_type = int(input())
contestants = list(map(int, input().split()))
score = 0

for answer in contestants:
	if answer == tea_type:
		score += 1
print(score)
