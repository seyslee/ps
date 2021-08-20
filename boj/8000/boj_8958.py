"""
  Written by Younsung Lee on Jul. 24. 2021.
  BOJ 8958 "Score"
"""

case = int(input())

for _ in range(case):
    ox = list(str(input()))
    score = 0
    total = 0
    for word in ox:
        if word == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)
