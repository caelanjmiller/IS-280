import math
import random

# Calculate the Square and Cube of a Random Number:
random_generated_number: int = random.randint(1,100)
print(f"The square of {random_generated_number} is: {math.pow(random_generated_number, 2)}")
print(f"The cube of {random_generated_number} is: {math.pow(random_generated_number, 3)}")

# Calculate the Square Root of a Random Number:
another_random_generated_number: int = random.randint(1,100)
print(f"Square Root of {random_generated_number} is: {math.sqrt(another_random_generated_number)}")

# Experiment with Randomness:
random_float: float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")
float_meets_constant: float = random_float * 6
print(f"Scaled random float between 0.0 and 100: {float_meets_constant}")

# Explore Math Constants:
print(math.pi)
print(f"Pi is a mathematical constant that is defined by the ratio of a circle's circumference to its diameter")
print(math.e)
print(f"e, or Euler's number, is the base of the natural log, which is quite important for investigating both exponential growth and decay")