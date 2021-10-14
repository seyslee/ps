"""
    Author  : Younsung Lee
    Date    : 2021-10-14
    Site    : BOJ
    Pr Num  : 10808
    Pr Info : 알파벳 개수
"""

word = input()
alphabets = [0] * 26
 
for i in word:
    alphabets[ord(i) - 97] = word.count(i)

for i in alphabets:
    print(i, end=" ")
