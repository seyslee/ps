"""
    Author  : Younsung Lee
    Date    : 2021-09-09
    Site    : BOJ
    Pr Num  : 5635
    Pr Info : 생일
"""

n = int(input())
bds = []

for _ in range(n):
	n, d, m, y = input().split()
	bds.append([n, int(d), int(m), int(y)])
bds.sort(key = lambda x:(x[3], x[2], x[1]))

print(bds[-1][0])
print(bds[0][0])
