"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 5217 "Sum of Pairs
"""

case = int(input())

for _ in range(case):
	n = int(input())
	print("Pairs for %d:" % n, end=" ")
	start = 1

	for i in range((n - 1) // 2):
		if i != 0:
			print(",", end=" ")
		print(start, n - start, end="")
		start += 1
	print()
