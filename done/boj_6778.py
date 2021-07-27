"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 6778 "Which Alien?"
"""

a = int(input())
e = int(input())

if a >= 3 and e <= 4:
	print("TroyMartian")
if a <= 6 and e >= 2:
	print("VladSaturnian")
if a <= 2 and e <= 3:
	print("GraemeMercurian")
