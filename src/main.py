

from utils import square, is_even, celsius_to_fahrenheit
#Enter a number and check if it's even or odd, and also convert Celsius to Fahrenheit 
number = int(input("Enter a number: "))
print("The square of the number is:", square((number)))
print(type(number))
print("Is the number even?", is_even(number))

# Printing the square of the number
number = input("Enter a number: ")
print(type(number))
print("The square of {number} is: {square(int(number))}")
print("Is the number even?", is_even(int(number)))

number = input("Enter a temperature in Celsius: ")
#print(f"{number} degrees Celsius is equal to {celsius_to_fahrenheit(float(number))} degrees Fahrenheit.")