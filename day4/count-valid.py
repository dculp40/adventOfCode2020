from cerberus import Validator

with open('batch.txt', 'r') as f:
    batch = f.readlines()

#Part 1
# batch = [x.strip() for x in batch]
# batch.append('')

# validCount = 0
# allFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
# fieldsMissing = allFields.copy()

# for line in batch:
#     for field in line.split():
#         fieldsMissing.remove(field[:3])
#     if line == '':
#         if len(fieldsMissing) == 0 or len(fieldsMissing) == 1 and fieldsMissing[0] == 'cid':
#             validCount += 1
#         fieldsMissing = allFields.copy() #reset fields

# print(validCount)

#Part 2
batch = [x.strip() for x in batch]
batch.append('')

passportSchema = {
    'byr': {'regex': '(19[2-8][0-9]|199[0-9]|200[0-2])'},
    'iyr': {'regex': '(201[0-9]|2020)'},
    'eyr': {'regex': '(202[0-9]|2030)'},
    'hgt': {'anyof': [{'regex': '(1[5-8][0-9]|19[0-3])cm'},{'regex': '(59|6[0-9]|7[0-6])in'}]},
    'hcl': {'regex': '#[0-9a-f]{6}'},
    'ecl': {'regex': '(amb|blu|brn|gry|grn|hzl|oth)'},
    'pid': {'regex': '[0-9]{9}'},
    'cid': {'required': False}
}
v = Validator(passportSchema, require_all=True)

validCount = 0
passport = {}
for line in batch:
    for field in line.split():
        formattedField = field.split(':')
        passport[formattedField[0]] = formattedField[1]
    if line == '':
        # print(passport)
        # print(v.validate(passport))
        # print(v.errors)
        if v.validate(passport):
            validCount += 1
        passport = {}

print(validCount)