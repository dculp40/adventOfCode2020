
with open('expenses.txt', 'r') as f:
    expenses = f.readlines()
expenses = [int(x.strip()) for x in expenses]

# Part 1
# for i in range(len(expenses)):
#     expense1 = expenses[i]
#     for expense2 in expenses[i+1:]:
#         if expense1 + expense2 == 2020:
#             print(expense1, expense2, expense1*expense2)

# Part 2
for i in range(len(expenses)):
    expense1 = expenses[i]
    for j in range(i+1, len(expenses)):
        expense2 = expenses[j]
        for k in range(j+1, len(expenses)):
            expense3 = expenses[k]
            if expense1 + expense2 + expense3 == 2020:
                print(expense1, expense2, expense3, expense1*expense2*expense3)