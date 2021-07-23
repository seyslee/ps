"""
  Written by Younsung Lee on Jul. 23. 2021.
  BOJ 2476 "주사위 게임"
"""

n = int(input())
max_prize_money = 0

for _ in range(n):
	a, b, c = map(int, input().split())
	prize_money = 0
	
	if a == b == c:
		prize_money = 10000 + a * 1000
	elif a == b or b == c:
		prize_money = 1000 + b * 100
	elif a == c:
		prize_money = 1000 + a * 100
	else:
		prize_money = max(a,b,c) * 100

	if max_prize_money < prize_money:
		max_prize_money = prize_money

print(max_prize_money)
