"""
  Written by Younsung Lee on Aug. 4. 2021.
  BOJ 20332 "Divvying Up"
"""

n = int(input())
li = str(input()).split(' ')
sum = 0

for i in range(n):
	sum += int(li[i])
if sum % 3 == 0:
	print("yes")
else:
	print("no")
