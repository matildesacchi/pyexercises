"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?s
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a number typed by the user
# 2. Process:the program counts from 1 to that number and checks if each one is odd or even
# 3. Out:a list of numbers, each one with "is odd" or "is even"
# 4. What happens on 0, on a negative number, on a very large number:
#    0: I show a message, because there is nothing to count
#    a negative number: I show the same message
#    a very large number: I show a message, because I set a limit of 100. 5000 lines are too many to read


# Your code below
n = int(input("Enter a number: "))
limit = 100

if n <= 0:
    print("Please enter a number bigger than 0")
elif n > limit:
    print("Too many numbers, the limit is", limit)
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")