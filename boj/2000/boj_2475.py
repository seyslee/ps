"""
  Written by Younsung Lee on Sep. 1. 2021.
  BOJ 2475 "검증수"
"""

sum = 0
for n in list(map(int, input().split())):
    sum += n ** 2
print(sum % 10)
