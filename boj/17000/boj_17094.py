"""
  Written by Younsung Lee on Aug. 3. 2021.
  BOJ 17094 "Serious Problem"
"""

s = int(input())
w = str(input())
score_2, score_e = 0, 0

for c in w:
    if c == "2":
        score_2 += 1
    elif c == "e":
        score_e += 1

if score_2 > score_e:
    print("2")
elif score_2 < score_e:
    print("e")
else:
    print("yee")
