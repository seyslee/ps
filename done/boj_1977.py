"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 1977 "완전제곱수"
"""

m = int(input())
n = int(input())
num = []
i = 1

while i ** 2 <= n:
    if m <= i ** 2 <= n:
        num.append(i ** 2)
    i += 1
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])
