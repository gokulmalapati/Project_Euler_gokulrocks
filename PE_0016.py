#Project Euler - Power Digit Sum

prod = 1
#To make 2^1000
for i in range(1000):
    prod*=2
sum = 0
#to add the sum of digits of 2^1000
while prod>0:
    sum +=prod%10
    prod = prod//10
print(sum)
