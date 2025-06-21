from pathlib import Path
from functools import reduce

path = Path("pg37239.txt")

count = 0
word = 'the '
for line in path.read_text("UTF-8").splitlines():
    count += line.lower().count(word)

def reducer(sum, line):
    return line.lower().count(word) + sum
c2 = reduce(reducer, path.read_text("UTF-8").splitlines(), 0 )
print(f"'{word}' appears {count} times")
print(c2)