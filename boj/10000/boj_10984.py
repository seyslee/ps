"""
  Written by Younsung Lee on Aug. 18. 2021.
  BOJ 10984 "내 학점을 구해줘"
"""

n = int(input())

for _ in range(n):
	m = int(input())
	total_c = 0
	total_g = 0
	
	for _ in range(m):
		c, g = map(float, input().split())
		total_c += c
		total_g += c * g
		
	gpa = total_g / total_c
	print(int(total_c), '%.1f' % (gpa))
