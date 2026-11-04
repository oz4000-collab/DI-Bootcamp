#Exercise 1:
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

#Solution 1:
my_fav_numbers = {7, 14, 21, 28, 35}
my_fav_numbers.add(78)
my_fav_numbers.add(99)
my_fav_numbers.remove(35)
friend_fav_numbers = {1, 2, 3}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#Exercise 2: 
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

#Solution 2:
my_tuple = (1,2,3,4,5)

#Exercise 3:
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

#solution 3:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
count = basket.count("Apples")
basket.clear()
print(basket)

#Exercise 4
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

#Solution 4
my_list = [1, 2, 3, 4, 5]
result = []
for num in my_list:
   result.append(num)
   result.append(num + 0.5)

#Exercise 5
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

#Solution 5
my_list1 = []
for i in range(1, 21):
    my_list1.append(i)
for index, item in enumerate(my_list1):
    if index % 2 == 0:
        print(my_list1[index]) 

#Exercise 6
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

#Solution 6
user_name = input("Enter your name: ")
while (len(user_name) < 3 or any(char.isdigit() for char in user_name)):
    print("give the correct name")
    user_name = input("Enter your name: ")
print("thank you")

#Exercise 7
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

#Solution 7
my_fav_fruits = []
user_input_fruit = input("Enter your favorite fruits: ")
my_fav_fruits =  user_input_fruit.split()
user_input_fruit1 = input("Enter the name of any fruit: ")
if user_input_fruit1 in my_fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


#Exercise 8
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

#Solution 8
base_price = 10
my_toppings = []
my_input_topping = input("Enter your favorite toppings: ")
while "quit" not in my_toppings:    
    print(f"Adding {my_input_topping} to your pizza.")
    my_toppings.append(input("Enter your favorite toppings: "))
print(f"Your final price is: {base_price + len(my_toppings) * 2.5}")

#Exercise 9
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

#Solution 9
ages = input("Enter the ages of the people in your family, separated by spaces: ")
ages_list = [int(age) for age in ages.split()]
if any(age <= 0 for age in ages_list):
    print(f"Thats the invalid age/s: {', '.join(str(age) for age in ages_list if age <= 0)}")
    ages_list = [age for age in ages_list if age > 0]
    print(f"Invalid age please fix it")
    ages_list = ages_list + [int(age) for age in input("Enter the ages of the people in your family, separated by spaces: ").split()]
count_between_3To12 = sum(1 for num in ages_list if 3 <= num <= 12)
count_above_12 = sum(1 for num in ages_list if num >= 12)
print(f"The total ticket cost is: {count_between_3To12 * 10 + count_above_12 * 15}")
 




