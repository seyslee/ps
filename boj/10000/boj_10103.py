"""
  Written by Younsung Lee on Jul. 25. 2021.
  BOJ 10103 "Double Dice"
"""

r = int(input())
score_a, score_b = 100, 100

for _ in range(r):
    a, b = map(int, input().split())
    if a > b:
        score_b -= a
    elif a < b:
        score_a -= b

print(score_a, end='\n')
print(score_b, end='')
