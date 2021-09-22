"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 1427
    Pr Info : 소트인사이드
"""

num_list = input()
num_list = [int(n) for n in num_list]

ordered_num_list = sorted(num_list, reverse=True)

for n in ordered_num_list : 
    print(n, end="")
