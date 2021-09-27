"""
    Author  : Younsung Lee
    Date    : 2021-09-27
    Site    : BOJ
    Pr Num  : 15792
    Pr Info : A/B - 2
"""

a, b = map(int, input().split())
print(a // b, end='')

if a % b:
    print('.', end='')
    i = 0
    
    while a % b and i < 1000:
        a = a % b * 10 
        i += 1
        print(a // b, end='')
