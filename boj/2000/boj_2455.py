"""
    Author  : Younsung Lee
    Date    : 2021-09-06
    Site    : BOJ
    Pr Num  : 2455
    Pr Info : 지능형 기차
"""

peoples = []
people = 0

for _ in range(4):
	op, ip = map(int, input().split())
	people -= op
	people += ip
	peoples.append(people)

print(max(peoples))
