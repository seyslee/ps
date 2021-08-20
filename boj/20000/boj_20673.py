"""
  Written by Younsung Lee on Aug. 9. 2021.
  BOJ 20673 "Covid-19"
"""

p = int(input())
q = int(input())

if p <= 50 and q <= 10:
	print("White")
elif q > 30:
	print("Red")
else:
	print("Yellow")
