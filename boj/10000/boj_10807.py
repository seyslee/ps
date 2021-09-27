"""
    Author  : Younsung Lee
    Date    : 2021-09-27
    Site    : BOJ
    Pr Num  : 10807
    Pr Info : 개수 세기
"""

c = int(input())
numbers = list(map(int, input().split()))
v = int(input())

print(numbers.count(v))
