#Project Euler - Counting Sundays

from datetime import date , timedelta

d = date(1901,1,1)
end = date(2000,12,31)
f_s = 0

while d <= end:
    if d.weekday() == 6 and d.day == 1:
        f_s +=1
    d += timedelta(days=1)

print(f_s)
