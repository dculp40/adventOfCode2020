with open('batch.txt', 'r') as f:
    batch = f.readlines()


#Part 1
batch = [x.strip() for x in batch]
batch.append('')

validCount = 0
allFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fieldsMissing = allFields.copy()

for line in batch:
    for field in line.split():
        fieldsMissing.remove(field[:3])
    if line == '':
        if len(fieldsMissing) == 0 or len(fieldsMissing) == 1 and fieldsMissing[0] == 'cid':
            validCount += 1
        fieldsMissing = allFields.copy() #reset fields

print(validCount)

