#Project Euler - Smallest multiple

lm =1
for x in [2,3,5,7,11,13,17,19]:
    primefac = x
    while(primefac*x <= 20):
        primefac = primefac*x
    lm *= primefac

print(lm)
