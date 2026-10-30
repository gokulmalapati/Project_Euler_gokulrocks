#Project Euler - Highly Divisible Triangular Number

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

product = 1
n = 2
trin = 0
while product <= 500:
    trin = n*(n+1)/2
    otrin = trin
    i = 2
    product = 1
    while i * i <= otrin:
        count = 1
        trin = otrin
        if is_prime(i):
            while(trin%i ==0):
                count +=1
                trin //=i
            product *= count
        i += 1
    n+=1

print(otrin)
