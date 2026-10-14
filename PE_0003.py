#Project Euler - Largest Prime Factor
#in which we find the required answer by checking all primes for divisibilty of rn in an increasing order
i = 2
rn = 600851475143
Lprimefac = 0
while i*i < rn :
    if rn%i == 0 :
        n=2
        prime = True
        while n*n <i :
            if i%n == 0:
                prime = False
            n+=1
        if prime:
            Lprimefac = i
    i +=1

print(Lprimefac)
