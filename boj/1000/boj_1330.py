"""
  Written by Younsung Lee on Aug. 3. 2021.
  BOJ 1330 "두 수 비교하기"
"""

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
