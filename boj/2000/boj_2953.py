"""
    Author  : Younsung Lee
    Date    : 2021-09-19
    Site    : BOJ
    Pr Num  : 2953
    Pr Info : 나는 요리사다
"""

scores = []

for _ in range(5):
    scores.append(sum(map(int, input().split())))
print(scores.index(max(scores)) + 1, max(scores))