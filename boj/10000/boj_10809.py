"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 10809
    Pr Info : 알파벳 찾기
"""

word = input()
alphabets = list(range(97, 123))

for i in alphabets:
	print(word.find(chr(i)), end=' ')
