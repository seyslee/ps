"""
  Written by Younsung Lee on Aug. 12. 2021.
  BOJ 21591 "Laptop Sticker"
"""

wc, hc, ws, hs = map(int, input().split())

if (wc - ws) >= 2 and (hc - hs) >= 2:
    print(1)
else:
    print(0)
