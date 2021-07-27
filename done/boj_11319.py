"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 11319 "Count Me In"
"""

case = int(input())
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(case):
	sentence = str(input())
	c, v = 0, 0
	for word in sentence:
		if word in vowels:
			v += 1
		elif word.isalpha():
			c += 1
	print(c, v)
