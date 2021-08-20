"""
  Written by Younsung Lee on Jul. 21. 2021.
  BOJ 10039 "Average Score"
"""

sum = 0

for _ in range(5):
	score = int(input())
	if score < 40:
		score = 40
		sum += score
	else:
		sum += score

print(sum // 5)
