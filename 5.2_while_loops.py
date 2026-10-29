"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the answers the user types, yes or no
# 2. Process:the program keeps asking if the budget is approved, until the user says yes or until 3 attempts are used
# 3. Out:a summary with the number of attempts and if the budget was approved or not
# 4. My stop condition, my attempt limit, my summary:#    stop condition: the user answers yes
#    attempt limit: 3 attempts, then the program stops anyway
#    summary: how many attempts were used, and if the budget was approved
#    I accept "Yes", "yes" and " yes " as the same answer, because I clean the answer with strip() and lower()

# Your code below
max_attempts = 3
attempts = 0
approved = False

while attempts < max_attempts and not approved:
    answer = input("Do you approve the Winter Sale budget? (yes/no): ")
    attempts = attempts + 1
    if answer.strip().lower() == "yes":
        approved = True

print("Summary")
print("Attempts used:", attempts)
if approved:
    print("The budget was approved")
else:
    print("The budget was not approved, the limit of", max_attempts, "attempts was reached")

# CHECK IT YOURSELF
# I answered no three times: the program stopped after 3 attempts and said the limit was reached. Correct
# I answered "  YES  " with capitals and spaces: the program accepted it at the first attempt. Correct
