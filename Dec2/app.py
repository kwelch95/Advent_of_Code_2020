
FILENAME = "input.txt"


with open(FILENAME,"r") as f:
    data = f.read()

pass_list = {}

for line in data.rsplit(" "):
    information = line
    pass_list[information[0]] = {'number': information[1], 'pass': information[2]}

print(pass_list)
