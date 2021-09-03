"""
  Written by Younsung Lee on Sep. 3. 2021.
  BOJ 2523 "점수계산"
"""

n = int(input())
sum = 0
result = 0
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0

print(result)