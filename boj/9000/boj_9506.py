"""
  Written by Younsung Lee on Jul. 24. 2021.
  BOJ 9506 "Federation Favorites"
"""

while True:
    n = int(input())
    factors = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    if sum(factors) == n:
        print(n, " = ", " + ".join(str(i) for i in factors), sep="")
    else:
        print(n, "is NOT perfect.")
