"""
    Author  : Younsung Lee
    Date    : 2021-09-23
    Site    : BOJ
    Pr Num  : 1157
    Pr Info : 단어 공부
"""

word = input().upper()
character_list = list(set(word))
cnt = []

for i in character_list:
	count = word.count(i)
	cnt.append(count)

if cnt.count(max(cnt)) >= 2:
	print("?")
else:
	print(character_list[cnt.index(max(cnt))])
