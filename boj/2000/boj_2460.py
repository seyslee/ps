"""
    Author  : Younsung Lee
    Date    : 2021-09-14
    Site    : BOJ
    Pr Num  : 2460
    Pr Info : 지능형 기차 2
"""

p = 0
pl = []

for i in range(10):
	o, i = map(int, input().split())
	p -= o
	p += i
	pl.append(p)

print(max(pl))
