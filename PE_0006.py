# Project Euler - Sum Square Difference

n = 100

s = (n*(n+1)/2) # This is the formula for sum of consecutive natural numbers.
sq_s = s*s
s_sq = n*(n+1)*(2*n+1)/6  #This is the formula for sum of squares of consecutive natural numbers.

Diff = sq_s - s_sq
print(Diff)
