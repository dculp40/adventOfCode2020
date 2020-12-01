
with open('expenses.txt', 'r') as f:
    expenses = f.readlines()
expenses = [int(x.strip()) for x in expenses]

for i in range(len(expenses)):
    expense1 = expenses[i]
    for expense2 in expenses[i+1:]:
        if expense1 + expense2 == 2020:
            print(expense1, expense2, expense1*expense2)