"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a dictionary that describes one marketing campaign, with five fields
# 2. Process:the program reads one field, changes the budget, removes one field, and then shows all the fields
# 3. Out:every field of the campaign with its value
# 4. My object, my five fields, and why those:my object is a marketing campaign. I chose name, channel, budget, month and target, because these are the things I need to know to plan a campaign and check it

# Your code below
campaign = {
    "name": "Winter Sale",
    "channel": "Instagram",
    "budget": 1500,
    "month": "December",
    "target": "students"
}

# read one field
print("Channel:", campaign["channel"])

# change one field
campaign["budget"] = 1800

# remove one field
del campaign["month"]

# show every field with its value
for field in campaign:
    print(field, ":", campaign[field])

# a field that does not exist
print("Results:", campaign.get("results", "not available"))

# CHECK IT YOURSELF
# When I asked campaign["results"], the program crashed with KeyError, because that field does not exist
# With campaign.get("results", "not available") the program does not crash and shows "not available"
