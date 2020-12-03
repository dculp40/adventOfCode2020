with open('map.txt', 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

#Part 1
height = len(content)
width = len(content[0])
pos = [0, 0]
trees = 0

while pos[1] < height - 1:
    pos[0] += 3
    pos[1] += 1
    if content[pos[1]][pos[0] % width] == '#':
        trees += 1

print(trees)