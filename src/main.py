

from utils import square, is_even, celsius_to_fahrenheit
#Enter a number and check if it's even or odd, and also convert Celsius to Fahrenheit 
number = float(input("Enter a number: "))
print(f"Square: {square(number)}")
print(f"Even: {is_even(number)}")
print(f"Celcius: {celsius_to_fahrenheit(number)}")