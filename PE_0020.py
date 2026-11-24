#Project Euler - Factorial Digit Sum

def fac(n):
    if n ==0:
        return 1
    else:
        return n*fac(n-1)

def sumd(n):
    sum = 0
    while(n>0):
        sum += n%10
        n //=10
    print(sum)


print(fac(100))
sumd(fac(100))
