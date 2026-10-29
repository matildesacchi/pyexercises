"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence typed by the user
# 2. Process: the program cleans the spaces at both ends with strip(), then applies four different string methods
# 3. Out: four versions of the same sentence, one per line. The original sentence stays untouched
# 4. My four transformations, and when each is useful:
#    strip(): removes spaces at both ends, useful to clean what a user types in a form
#    upper(): all capital letters, useful for codes or headings, like a currency code "GBP"
#    title(): capitalises each word, useful to format names, like "matilde sacchi" into "Matilde Sacchi"
#    replace(" ", "_"): replaces spaces with underscores, useful to turn a title into a file name

# Your code below
text = input("Enter a sentence: ")

print("original   :", repr(text))
print("strip()    :", repr(text.strip()))
print("upper()    :", text.strip().upper())
print("title()    :", text.strip().title())
print("replace()  :", text.strip().replace(" ", "_"))

# CHECK IT YOURSELF (input: "   hello Matilde sacchi   ")
# strip(): expected, 'hello Matilde sacchi' without the spaces at both ends
# upper(): expected, HELLO MATILDE SACCHI
# title(): expected, Hello Matilde Sacchi, every word starts with a capital
# replace(): expected, hello_Matilde_sacchi, no underscores at the ends because strip() came first