# ============================================================
# CODEFORCES — 1328A | Divisibility Problem
# ============================================================
# Time limit:   1 second
# Memory limit: 256 MB
#
# PROBLEM STATEMENT
# -----------------
# Given two positive integers a and b, in one move you can
# increase a by 1 (a = a + 1).
#
# Find the minimum number of moves required to make a
# divisible by b.
#
# If a is already divisible by b, no moves are required.
#
# INPUT
# -----
# t: number of independent test cases.
# For each test case, two positive integers a and b.
#
# OUTPUT
# ------
# For each test case, print the minimum number of moves.
#
# CONSTRAINTS
# -----------
# 1 <= t <= 10^4
# 1 <= a, b <= 10^9
#
# EXAMPLE
# -------
# Input:                 Output:
# 5
# 10 4                   2
# 13 9                   5
# 100 13                 4
# 123 456                333
# 92 46                  0
#
# ============================================================

t = int(input())
answer = []

for _ in range(t):
    a,b = map(int, input().split())
    r = a%b                                     # Save r=a%b for optimization
    answer.append(str(b - r if r!=0 else 0))    # If r==0 then it's trivial,
                                                # otherwise we know that a=bq+r for some q,r in Z.
                                                # So r=a-bq and we're searching for x such that a+x=bk for some k in Z.
                                                # If we choose x = b-r = b-a+bq = b*(1+q) - a then we get:
                                                # a + x = a + b(1+q) - a = b(1+q) with 1+q in Z.

print('\n'.join(answer))

