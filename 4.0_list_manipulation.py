"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DOo
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a list of 8 monthly marketing budgets, in euros
# 2. Process: the program shows the list, picks one month, sorts the list and calculates the total and the average
# 3. Out:the whole list, one budget, the sorted list, the total and the average
# 4. What my list is about, and what I computed from it:What my list is about, and what I computed from it: my list is the marketing budget for 8 months. I computed the total and the average, because they show how much we spend in total and how much we spend in a normal month


# Your code below
budgets = [1200, 950, 1500, 800, 1100, 1300, 900, 1000]

print("All budgets:", budgets)
print("Budget of month 3:", budgets[2])
print("Sorted budgets:", sorted(budgets))

total = sum(budgets)
average = total / len(budgets)

print("Total:", total)
print("Average:", average)
print("Check, total of the first three months:", budgets[0] + budgets[1] + budgets[2])

# CHECK IT YOURSELF
# By hand, the first three months: 1200 + 950 + 1500 = 3650
# The program also says 3650. Correct
