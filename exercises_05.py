# ============================
#
# Part 1: Lists
#
# ============================

# We will be working with this list of names
names = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]

# Exercise 1: I missed the name "George". Add it to the list.
...
print("Names with 'George' added:", names)
names = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]
names.append("George")
print("Names with 'George' added:", names)


# Exercise 2: I prefer 'Alexander' to 'Alex'. Change that in the list
...
print("Names with 'Alex' changed:", names)
print()
names = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]
names = ["Alexander" if name == "Alex" else name for name in names]

print("Names with 'Alex' changed:", names)


# Exercise 3: Make another list which contains only those names which start with A
names = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]
names_starting_with_A = [name for name in names if name.startswith('A')]

print(names_starting_with_A)



# Exercise 4: Give me a list which contains the first three letters of each name sorted alphabetically
names = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]
first_three_letters = [name[:3] for name in names]
first_three_letters_sorted = sorted(first_three_letters)
print("First three letters of each name sorted alphabetically:", first_three_letters_sorted)

# Exercise 5: Which names from this list are not in the original list
names_to_look_for = ["Anna", "Jack", "Stu", "Felix", "Amy"]
names_not_in_list = ["Alice", "Bob", "Anna", "David", "Alex", "Amy", "Ben", "Adam"]
print("These names are not in the original list:", names_not_in_list)
print()


# ============================
#
# Part 2: Dicts
#
# ============================

# Exercise 6: How long would I need to see all the films in one go?
film_runtimes = {
    "The Godfather": 175,
    "The Shawshank Redemption": 142,
    "Pulp Fiction": 154,
    "The Dark Knight": 152,
    "12 Angry Men": 96
}

total_runtime = sum(film_runtimes.values())
print("Total runtime of all films in one go:", total_runtime, "minutes")
print()


# Exercise 7: One of the runtimes (12 Angry men) is wrong. It should be 97 minutes. Fix it.
...
print("Fixed runtime for '12 Angry Men':", film_runtimes["12 Angry Men"], "minutes")
print()

# Exercise 8: You have a list of film titles I want to see. Give me a dictionary with the runtimes of those films.
# If you don't know how long a film is, put None
film_titles = ["The Godfather", "The Shawshank Redemption", "The Dark Knight", "Inception", "Interstellar"]

film_runtimes_selected = {
    "The Godfather": 175,  # minutes
    "The Shawshank Redemption": 142,  # minutes
    "The Dark Knight": 152,  # minutes
    "Inception": 148,  # minutes
    "Interstellar": None  # runtime not found
}
print("Dictionary with runtimes of selected films:", film_runtimes_selected)
print()


# ============================
#
# Part 3: Sets
#
# ============================

# Exercise 9: Print all the characters (without repetition) which are used in the film titles we have, in alphabetical
# order
film_titles = [
    "The Godfather",
    "Pulp Fiction",
    "The Dark Knight",
    "Forrest Gump",
    "Inception"
]
unique_characters = set(film_titles)
unique_characters_sorted = sorted(unique_characters)

# Convert the set to a sorted list and print
print("Unique characters used in film titles:", sorted(unique_characters))
print()

# ============================
#
# Part 4: Tuples
#
# ============================

# Exercise 10: Uncomment the code below and run it. You will get some errors. Think about why you are getting them and
# fix them

film_runtimes_with_details = {
    ("Monthy Python And The Holy Grail", "comedy"): 95,
    ("The Godfather", ("crime", "drama")): 175,
}
print(f"Total runtime: {sum(film_runtimes_with_details.values())}")

# ============================
#
# Part 5: Comprehensions
#
# ============================

# Rewrite the solutions to these exercises using comprehensions: 4, 3, 8 and (optionally) 9

# 3
names_starting_with_A =[name for name in names if name.startswith('A')]

# 4
first_three_letters = [name[:3] for name in names]

# 8
film_runtimes =[175, 142, 152, 148]
film_runtimes_selected = [runtime for runtime in film_runtimes if runtime in film_runtimes_selected]
# 9
unique_characters = {char for char in first_three_letters}
