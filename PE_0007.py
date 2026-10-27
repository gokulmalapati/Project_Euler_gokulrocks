# Project Euler - 10001st Prime Number.

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

n = 1
prime = 0
while(prime<10001):
    if is_prime(n):
        prime+=1
    n+=1

print(n-1)
