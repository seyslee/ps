"""
    Author  : Younsung Lee
    Date    : 2021-09-17
    Site    : BOJ
    Pr Num  : 2920
    Pr Info : 음계
"""

scales = list(map(int, input().split()))

if scales == sorted(scales):
	print("ascending")
elif scales == sorted(scales, reverse=True):
	print("descending")
else:
	print("mixed")
