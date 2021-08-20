"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 14038 "Tournament Selection"
"""

score = 0

for _ in range(6):
	result = str(input())
	if result == 'W':
		score += 1

if score >= 5:
	print(1)
elif score >= 3:
	print(2)
elif score >= 1:
	print(3)
else:
	print(-1)
