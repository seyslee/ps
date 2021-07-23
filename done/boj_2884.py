"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 2884 "SPAVANAC"
"""

h, m = map(int, input().split())

if m >= 45:
	m -= 45
elif m < 45:
	if h == 0:
		h = 23
	else:
		h -= 1
	m += 60
	m -= 45
	
print(h, m)
