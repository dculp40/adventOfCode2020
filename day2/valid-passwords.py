with open('passwords.txt', 'r') as f:
    content = f.readlines()


#Part 1
# validCount = 0
# for line in content:
#     splitLine = line.replace('-', ' ').split()
#     match = splitLine[2][0]
#     i = 0
#     for letter in splitLine[3]:
#         if letter == match: i+=1
#     if i >= int(splitLine[0]) and i <= int(splitLine[1]):
#         validCount += 1

# print(validCount)

validCount = 0
for line in content:
    splitLine = line.replace('-', ' ').split()
    match = splitLine[2][0]
    i = 0
    pw = splitLine[3]
    if pw[int(splitLine[0]) - 1] == match: i+=1
    if pw[int(splitLine[1]) - 1] == match: i+=1
    if i == 1:
        validCount += 1

print(validCount)