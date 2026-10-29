"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:my list of 8 monthly marketing budgets from exercise 4.0
# 2. Process:the program goes through the list one budget at a time, and for each one calculates its share of the total
# 3. Out:8 lines, one for each month, with the month number, the budget and its percentage of the total
# 4. What I compute for each item, and why it is worth showing:the percentage of the total budget. It shows which months take the biggest part of the money, for example month 3 is the most expensive


# Your code below
budgets = [1200, 950, 1500, 800, 1100, 1300, 900, 1000]
total = sum(budgets)

for position, budget in enumerate(budgets, start=1):
    share = budget / total * 100
    print(f"Month {position}: {budget} euros, {round(share, 1)}% of the total")

# CHECK IT YOURSELF
# I count 8 lines, the same as the 8 items in my list. No off-by-one