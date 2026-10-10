#Project Euler - Fibonacci Numbers
# sum of even terms of fibonacci series till the terms reach 4000000
i = 1
sum = 0
n=1
series=[]
while i <= 4000000:
    if i%2 == 0:
        sum+=i
    series.append(i)
    if n-1>=0 and n-2>=0:
        i = series[n-1] + series[n-2]
    else:
       i = i + series[n-1]

    n +=1

print(sum)
