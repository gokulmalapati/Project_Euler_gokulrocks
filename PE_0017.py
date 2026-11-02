#Project Euler - Number Letter Counts
from num2words import num2words
import re

words = ""
for i in range(1,1001):
    words = words + num2words(i)
letters = re.findall(r"[a-zA-Z]",words)
print(len(letters))
