#Project Euler - Largest Palindrome Number


def palincheck(N):
    N = str(N)
    return N == N[::-1]

x = 979
max_p = 0
while x>900:
    y = 999
    while y > 900:
        z = x*y
        if palincheck(z):
            max_p = max(max_p,z)
        y-=1
    x-=11
print(max_p)
