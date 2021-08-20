"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 10102 "Vote Count"
"""

v = int(input())
list = list(input())
a_vote_num = 0
b_vote_num = 0

for i in range(v):
	if list[i] == "A":
		a_vote_num += 1
	elif list[i] == "B":
		b_vote_num += 1

if a_vote_num > b_vote_num:
	print("A")
elif a_vote_num < b_vote_num:
	print("B")
else:
	print("Tie")
