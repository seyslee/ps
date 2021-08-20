"""
  Written by Younsung Lee on Jul. 28. 2021.
  BOJ 13752 "히스토그램"
"""

case = int(input())
for _ in range(case):
	result = ""
	k = int(input())
	for _ in range(k, 0, -1):
		result += '='
	print(result)
