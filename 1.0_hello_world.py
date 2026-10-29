"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.gua

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a text message and the number of times to repeat it
# 2. Process:the program repeats the message in a loop, adding the line number each time
# 3. Out:the message printed on screen five times, each line numbered from 1 to 5
# 4. My message, and why:"Hello, [tuo nome]!" because it is my first program, and I want it to greet me personally instead of the generic "Hello, World!"
nome = "Matilde"
for i in range (5):
    print(nome)

# Your code below
print("Hello, Matilde!")


for i in range( 5 ) :
    print("Hello, Matilde!")