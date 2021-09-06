"""
    Author  : Younsung Lee
    Date    : 2021-09-06
    Site    : BOJ
    Pr Num  : 1546
    Pr Info : 평균
"""

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

for i in range(n):
	scores[i] = scores[i] / max_score * 100
	avg = sum(scores) / n
print("%.2f" % avg)
