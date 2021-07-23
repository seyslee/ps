"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 7567 "그릇"
"""

dishes = list(str(input()))
height = 0

for i in range(len(dishes)):
	if i == 0:
		height += 10
	elif dishes[i] == dishes[i-1]:
		height += 5
	else:
		height += 10

print(height)
