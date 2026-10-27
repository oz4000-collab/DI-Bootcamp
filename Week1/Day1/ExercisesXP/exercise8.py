# Exercise 8: What’s your name?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
user_name = input("What's your name? ")
my_name = "Lee"
if user_name == my_name:
    print("Wow, we have the same name! That's funny!")
else:
    print(f"Nice to meet you, {user_name}!")