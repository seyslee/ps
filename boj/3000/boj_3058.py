"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 3058
    Pr Info : 짝수를 찾아라
"""

n = int(input())

for _ in range(n):
	num_list = list(map(int, input().split()))
	even_list = []

	for i in num_list:
		if i % 2 == 0:
			even_list.append(i)
	print(sum(even_list), min(even_list))
