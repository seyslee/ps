"""
  Written by Younsung Lee on Jul. 27. 2021.
  BOJ 9713 "Sum of Odd Sequence"
"""

case = int(input())

for _ in range(case):
    num = int(input())
    print(sum([n for n in range(1, num+1) if n%2]))
