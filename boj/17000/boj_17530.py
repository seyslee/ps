"""
  Written by Younsung Lee on Aug. 3. 2021.
  BOJ 17530 "Buffoon"
"""

n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

if li[0] == max(li):
    print("S")
else:
    print("N")
