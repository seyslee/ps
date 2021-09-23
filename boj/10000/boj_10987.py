"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 10987
    Pr Info : 모음의 개수
"""

cnt = 0
for i in input():
	if i in ['a', 'e', 'i', 'o', 'u']:
		cnt += 1
print(cnt)
