with open('passes.txt', 'r') as f:
    content = f.readlines()

#Part 1
maxID = -1
for bpass in content:
    lower = 0
    upper = 127
    for i in range(7):
        if(bpass[i] == 'F'):
            upper -= (upper - lower) / 2 + 1
        else:
            lower += (upper - lower) / 2 + 1

    left = 0
    right = 7
    for i in range(7,10):
        if(bpass[i] == 'L'):
            right -= (right - left) / 2 + 1
        else:
            left += (right - left) / 2 + 1
    bpassID = lower * 8 + left
    maxID = max(maxID, bpassID)

print(maxID)
