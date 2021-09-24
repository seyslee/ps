"""
    Author  : Younsung Lee
    Date    : 2021-09-24
    Site    : BOJ
    Pr Num  : 11721
    Pr Info : 열 개씩 끊어 출력하기
"""

word = input()

for i in range(0, len(word), 10):
	print(word[i:i+10])
