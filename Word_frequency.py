import string
from pathlib import Path
import re
from collections import Counter


p = Path("Word_frequency.txt")

with p.open("r") as file:
    text = str(file.read()).replace(',', ' ').replace('"', '').replace("'", '').replace('.', '').replace("\n", '').lower()

letters = list(string.ascii_lowercase)
for word in text.split():
   if word.isnumeric():
       continue
   else:
       letters.append(word)

print(Counter(letters).most_common(10))


