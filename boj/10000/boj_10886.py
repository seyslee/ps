"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 10886 "0 = not cute / 1 = cute"
"""

n = int(input())
cute = 0
ncute = 0

for _ in range(n):
	p = int(input())

	if p == 0:
		ncute += 1
	elif p == 1:
		cute += 1

if cute > ncute:
	print("Junhee is cute!")
elif ncute > cute:
	print("Junhee is not cute!")
