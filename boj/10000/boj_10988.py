"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 10988 "팰린드롬인지 확인하기"
"""

word = list(str(input()))

if list(reversed(word)) == word:
	print(1)
else:
	print(0)
