# Exercise 1: Online Shopping Discount

# Given a variable `total_amount` representing the total amount in the shopping cart,
# write a program that prints a discount message if the total amount is over $100,
# and always prints a thank you message.

total_amount = 120  # Fill in the total amount here

if total_amount > 100:
    print("Congratulations! You get a discount.")
print("Thank you for shopping with us!")

# Exercise 2: Temperature Checker

# Given a variable `temperature` representing the current temperature in Celsius,
# write a program that prints "Warm" if the temperature is greater than or equal to 25 degrees Celsius,
# otherwise print "Cool".

temperature = 22  # Fill in the temperature here

if temperature >= 25:
    print("Warm")
else:
    print("Cool")

# Exercise 3: Time of the Day

# Given a variable `hour` representing the current hour (in 24-hour format),
# write a program that prints "Good Morning" if the hour is before 12 (12 inclusive),
# "Good Afternoon" if the hour is between 12 and 17 (17 inclusive),
# and "Good Evening" if the hour is after 17.

hour = 15  # Fill in the hour here

if hour <= 12:
    print("Good Morning")
elif 12 < hour <= 17:
    print("Good Afternoon")
else:
    print("Good Evening")

# Exercise 4: Secret Message

# Given a variable `message` representing a secret message,
# write a program that prints "Message found" if the message is not empty,
# otherwise print "No message".

message = ""  # Fill in the message her
if message:
    print("Message found")
else:
    print("No message")


# Exercise 5: List Iteration

# You have a list of fruits. Write a program that iterates over each fruit in the list and prints each fruit's name.

fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]

for fruit in fruits:
    print(fruit)

# Exercise 6: Range Iteration

# Write a program that prints all the even numbers from 1 to 20 using a for loop and the range() function.
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
# Exercise 7: While Loop

# Write a program using a while loop to find the sum of all numbers from 1 to 100.

sum = 0
number = 1

# Use a while loop to iterate through numbers from 1 to 100
while number <= 100:
    sum += number
    number += 1

print("The sum of all numbers from 1 to 100 is:", sum)

# Exercise 8: Number of Friends

# Write a program that asks how many friends you have and then asks for each of their names.
# Ask the user for the number of friends
num_friends = (input("How many friends do you have? "))

# Initialize an empty list to store the names
friend_names = []

# Loop to get each friend's name
for i in range(num_friends):
    name = input(f"Enter the name of friend {i + 1}: ")
    friend_names.append(name)

# Print the list of friends' names
print("Your friends are:")
for name in friend_names:
    print(name)


# Exercise 9: Guess the Number
# Write a program that has a number and keeps asking the user to input a number until the user guesses it.

secret_number = 42
while True:
    guess = (input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again!")




# Exercise 10: Multiplication Table

# Generate the multiplication table for the numbers 1 to 9.

def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}", end="\t")
            print_multiplication_table()


# Exercise 11: continue

# Do the same as in Exercise 6 but do not print the number 10. Use `continue` do achieve this

for i in range(1, 21):
    if i == 10:
        continue
    print(i)

# Exercise 12: Password Checker

# Write a program that asks the user to enter a password. If the password is correct, print a message saying
# "Access granted" and end the program. If the user enters the wrong password three times, print "Access denied" and
# end the program..

correct_password = "learnpythonwithskillo"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

if attempts == 3:
    print("Access denied")

