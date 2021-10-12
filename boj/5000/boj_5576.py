"""
    Author  : Younsung Lee
    Date    : 2021-10-12
    Site    : BOJ
    Pr Num  : 5576
    Pr Info : 콘테스트
"""

wu = sorted([int(input()) for _ in range(10)])[7:]
ku = sorted([int(input()) for _ in range(10)])[7:]
print(sum(wu), sum(ku))
