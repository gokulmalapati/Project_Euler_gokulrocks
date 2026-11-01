#Project Euler - Longest Collatz Sequence

m_count = 1
i = 999999
while i > 0:
    count = 1
    oi = i
    while i != 1:
        if i%2 == 0:
            i = i/2
            count +=1
        else:
            i = 3*i + 1
            count+=1
    i = oi
    if count > m_count:
        m_count = count
        mi = i
    i-=1
print(mi)
