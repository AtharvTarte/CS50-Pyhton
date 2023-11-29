# store the file in array
names = []

with open ("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

print(sorted(names))