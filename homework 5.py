#1
numbers = list(range(1, 11))
print(numbers)

#1.1
numbers = list(range(1, 1001))
print(numbers)

#2
numbers = list(range(1, 11))
print("original list:", numbers)
reversed_numbers = numbers[::-1]
print("reversed list:", reversed_numbers)

#3
words = ["apple", "banana", "cherry", "kiss"]
lengths = [len(word) for word in words]
print(lengths)
#3.1
words_lengets = {word: len(word) for word in words}
print(words_lengets)


#4
def sum_of_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers))


#5
def find_min_max(t):
    min_val = t[0]
    max_val = t[0]

    for num in t:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val


t = (3, 1, 4, 1, 5, 9, 2, 6, 3, 10)
min_val, max_val = find_min_max(t)

print(f"minimum value is: {min_val}")
print(f"maximum value is: {max_val}")

#6
queue = []


def enqueue(item):
    queue.append(item)
    print(f"enqueued item is: {item}")


def dequeue():
    if len(queue) == 0:
        return "queue is empty"
    return queue.pop(0)


enqueue("apple")
enqueue("banana")
enqueue("cherry")
print(f"dequeued item is: {dequeue()}")
print(f"dequeued item is: {dequeue()}")
print(f"dequeued item is: {dequeue()}")
print(f"dequeued item is: {dequeue()}")

#7
students_accaunts = {"Alice": ["123456789", "987654321"], "Bob": ["111222333"]}
print(students_accaunts)
alice_account = students_accaunts["Alice"]
print("Alice`s accounts:", alice_account)


#8
def hash_list(lst):
    return hash(tuple(lst))


my_list = [1, 2, 3, 4, 5]
print(f"The hash of the list {my_list} is: {hash_list(my_list)}")

another_list = [10, 20, 30]
print(f"The hash of the list {another_list} is: {hash_list(another_list)}")

#9
string = "Sling Academy ball box Sling box ball Academy hello hello hello"
word_list = string.split()

word_frequency = {}
for word in word_list:
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, count in word_frequency.items():
    print(f"{word}: {count}")

#10
# Define two sets with some common elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection = set1.intersection(set2)
print("The intersection of set1 and set2 is:", intersection)

intersection = set1 & set2
print("The intersection of set1 and set2 is:", intersection)

#11
def is_subset(set_a, set_b):
    return (set_a.issubset(set_b))

set1 = {1, 2, 3,}
set2 = {1, 2, 3, 4, 5}
print(is_subset(set1, set2))
# output: True
print(is_subset(set2, set1))
# output: False

#12

#13
squares_of_even_numbers = [x**2 for x in range(1, 31) if x % 2 == 0]
print(squares_of_even_numbers)

#14
words = ["watermelon", "tree", "moon", "pants"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

#15
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = {x for x in range(2, 100) if is_prime(x)}

print(primes)


