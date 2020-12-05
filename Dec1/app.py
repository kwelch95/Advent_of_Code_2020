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

combos = combinations(numbers,2)
#print(list(combos))

for x, y in combos:
    sums = x + y
    if sums == 2020:
        print(x, y, x * y)
        break

