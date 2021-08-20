"""
  Written by Younsung Lee on Jul. 21. 2021.
  BOJ 2675 "Repeating Characters"
"""
 
t = int(input())

for _ in range(t):
	cnt, word = input().split()
	for x in word:
		print(x * int(cnt), end='')
	print()
