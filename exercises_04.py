# Exercise 1: Write a function to: Print numbers from 5 to 19
def print_numbers():
    for number in numbers:
        print(number)
        numbers = range(5, 20)
    print_numbers()


# Exercise 2: Write a function to:  Calculate the factorial of a number
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
        print(result)
        print(i)


# Exercise 3: Write a function to: Check if element is in a list. It should return True or False
def check_element_in_list(element, lst):
    ...


# Exercise 4: Write a function to: Check if a given name starts with a vowel. It should return True or False
def starts_with_vowel(name):
    ...


# Exercise 5: Write a function which takes in a list of numbers and gives me back another list with only the even ones
def extract_even_numbers(numbers):
    ...


print("\nTesting check_element_in_list() function:")
assert check_element_in_list(3, [1, 2, 3, 4, 5]), ("check_element_in_list() failed for element present in"
                                                   " the list")
assert not check_element_in_list(6, [1, 2, 3, 4, 5]), ("check_element_in_list() failed for element not present in"
                                                   " the list")
print("check_element_in_list() function passed the test.")

# Testing starts_with_vowel() function
print("\nTesting starts_with_vowel() function:")
assert starts_with_vowel("Alice"), "starts_with_vowel() failed for name starting with a vowel"
assert not starts_with_vowel("Bob"), "starts_with_vowel() failed for name not starting with a vowel"
print("starts_with_vowel() function passed the test.")

# Testing extract_even_numbers() function
print("\nTesting extract_even_numbers() function:")
assert extract_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10], ("extract_even_numbers() failed for "
                                                                                   "list with even numbers")
assert extract_even_numbers([11, 13, 15, 17, 19]) == [], "extract_even_numbers() failed for list with no even numbers"
assert extract_even_numbers([]) == [], "extract_even_numbers() failed for empty list"
assert extract_even_numbers([-2, -1, 0, 1, 2, 3]) == [-2, 0, 2], ("extract_even_numbers() failed for list with negative"
                                                                  " numbers")
print("extract_even_numbers() function passed the test.")
print("All tests passed!")