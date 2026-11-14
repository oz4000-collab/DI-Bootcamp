
# challeng1:
# Instructions:
# 1. Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

#challenge1 solution
x, y = map(int, input(f'Please enter a number and a length separated by a space:').split())
for item in range(x, x*y, x):
    print(item)


#challenge2
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# # 3. The program should print the modified string.


#challenge2 solution:    
user_input = list(input("Please enter a string:"))
kept_items = user_input[:1]

for i, item in enumerate(user_input[1:], start=1):
    if item != user_input[i - 1]:
        kept_items.append(item)

print("".join(kept_items))


