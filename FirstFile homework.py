 #1
import math
print("Hello, World!")

 #2
name = input("Victoria")
age = input("34")
favorite_color = input("grey")
print("My name is" +name+ "I’m" +age+ "years old" +favorite_color)

 #3
def area_simple_multiplication(length, width):
    return length * width
length =5
width =8
result = area_simple_multiplication(length, width)
print(f"Area of Rectangle: {result}")





 #4
def farenheit_to_celcius(num):
    celcius = (farenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celcius, 3))
farenheit = 40
farenheit_to_celcius(farenheit)
print("Temperature in Celsius:")

 #6
def calculate(radius=1.0):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

default_area, default_circumference = calculate()
print(f"Default Area: {default_area}")
print(f"Default Circumference: {default_circumference}")

 #7
a = 4
if a == (a > 1) < 1:
    print("Even:", a)
    print("Odd:", a)

 #8
x = input('Enter your age:65 ')
x = float(18)
if x > 18:
    print('Voter')
else:
    print('Non Voter')











