from itertools import combinations

FILENAME = "input.txt"


with open(FILENAME,"r") as f:
    data = f.read()

#print(repr(data))

numbers = []

for line in data.splitlines():
    #print(repr(line))
    number = int(line)
    numbers.append(number)

combos = combinations(numbers,3)
#print(list(combos))

for x, y, z in combos:
    sums = x + y + z
    if sums == 2020:
        print(x, y, z, x * y * z)
        break

