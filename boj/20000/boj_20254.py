"""
  Written by Younsung Lee on Aug. 4. 2021.
  BOJ 20254 "Site Score"
"""

ur, tr, uo, to = map(int, input().split())
score = 56 * ur + 24 * tr + 14 * uo + 6 * to
print(score)
