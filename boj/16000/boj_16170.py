"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 16170 "오늘의 날짜는?"
"""

import datetime
now = datetime.datetime.now() + datetime.timedelta(hours=9)
print(now.year)
print(now.month)
print(now.day)
