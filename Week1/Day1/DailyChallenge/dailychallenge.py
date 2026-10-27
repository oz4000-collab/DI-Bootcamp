# Instructions:
# 1. Ask for User Input:

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:

# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively

#Solution:
import random


user_input=input("Please enter a string of 10 characters:")
while len(user_input) != 10:
    if len(user_input) < 10:
        print("String not long enough.")
    else:
        print("String is too long.")

    user_input = input("Try again: ")

print("Perfect string.")
list_chars = list(user_input)
print("The first character in your string is:", list_chars[0])
print("The last-1 character in your string is:", list_chars[-1])
toconcat = ""
for item in list_chars:
    toconcat += item
    print(toconcat)

list_to_shuffle = list(user_input)
random.shuffle(list_to_shuffle)
print("The shuffled string is:", ''.join(list_to_shuffle))

    
    