# Project Euler - Summation of Primes

def is_prime(n):
    if n< 2:
        return 0
    if n==2 or n==3:
        return 1
    if n%2 == 0 or n%3 == 0:
        return 0
    x = 2
    while x*x <= n :
        if n%x == 0:
            return 0
        x+=1
    return 1

y = 1
sum_p = 0
while y <= 2000000:
    if is_prime(y):
        sum_p += y
    y+=1
print(sum_p)
