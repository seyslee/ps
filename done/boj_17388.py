"""
  Written by Younsung Lee on Aug. 3. 2021.
  BOJ 17388 "와글와글 숭고한"
"""

s, k, h = map(int, input().split())
total_score = s + k + h

if total_score >= 100:
    print("OK")
elif total_score < 100:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    else:
        print("Hanyang")

