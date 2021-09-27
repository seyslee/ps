"""
    Author  : Younsung Lee
    Date    : 2021-09-27
    Site    : BOJ
    Pr Num  : 5800
    Pr Info : 성적 통계
"""

c = int(input())

for i in range(c):
	scores = sorted(list(map(int, input().split()))[1:])
	gaps = []
	print(f'Class {i + 1}')
	for j in range(len(scores) - 1):
		gaps.append(scores[j + 1] - scores[j])
	print(f'Max {max(scores)}, Min {min(scores)}, Largest gap {max(gaps)}')
