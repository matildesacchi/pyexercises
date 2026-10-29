"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:my list of 8 monthly marketing budgets from exercise 4.0
# 2. Process:the program shows the list in four different orders, without changing the original
# 3. Out:four versions of the list, and at the end the original list, still the same
# 4. My four orders, and which ones modify the original:#    1. original order: just the list as I wrote it
#    2. smallest to biggest: with sorted(), it makes a new list, so the original does not change
#    3. biggest to smallest: with sorted(..., reverse=True), also a new list
#    4. last month first: with .reverse(), which changes the list itself. So I used it on a copy, not on the original

# Your code below
budgets = [1200, 950, 1500, 800, 1100, 1300, 900, 1000]

print("1. Original order:", budgets)
print("2. Smallest to biggest:", sorted(budgets))
print("3. Biggest to smallest:", sorted(budgets, reverse=True))

budgets_copy = budgets.copy()
budgets_copy.reverse()
print("4. Last month first:", budgets_copy)

print("Original at the end:", budgets)

# CHECK IT YOURSELF
# The last line shows [1200, 950, 1500, 800, 1100, 1300, 900, 1000]
# It is the same as my list in 4.0, item by item. Correct, the original was not damaged