"""
    Author  : Younsung Lee
    Date    : 2021-09-29
    Site    : BOJ
    Pr Num  : 9076
    Pr Info : 점수 집계
"""

n = int(input())
for _ in range(n):
    points = list(map(int, input().split()))
    points.remove(max(points))
    points.remove(min(points))
    if max(points) - min(points) >= 4:
        print('KIN')
    else:
        print(sum(points))
