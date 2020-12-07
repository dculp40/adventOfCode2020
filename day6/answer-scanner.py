with open('answers.txt', 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

#Part 1
# groupID = 0
# groups = {}

# for row in content:
#     if row == '': groupID +=1
#     else:
#         for answer in row:
#             if groupID in groups:
#                 groups[groupID].add(answer)
#             else:
#                 groups[groupID] = {answer}

# yesCount = 0
# for group in groups.values():
#     yesCount += len(group)
# print(yesCount)

# Part 2
groupID = 0
groups = {}

for row in content:
    if row == '': groupID +=1
    elif groupID in groups:
        for answer in groups[groupID].copy():
            if answer not in row:
                groups[groupID].remove(answer)
    else:
        groups[groupID] = set()
        for answer in row:
            groups[groupID].add(answer)

yesCount = 0
for group in groups.values():
    yesCount += len(group)
print(yesCount)