# User input for miles driven, gallons of gas used & cost of gas
milesDriven: int = int(input("Enter the Miles Driven: "))
gallonsUsed: int = int(input("Enter Gallons of Gas Used: "))
gasCost: float = float(input("Enter Cost Per Gallon: "))

# Calculate miles per gallon
mpg: float = milesDriven / gallonsUsed
print(f"Miles Per Gallon: {mpg:.1f}")

# Calculate total cost of gas for this trip
total: float =  gallonsUsed * gasCost
print(f"Total Gas Cost: {total:.1f}")

# Calculate gas cost per mile
costPerMile: float = total / milesDriven
print(f"Cost Per Mile: {costPerMile:.1f}")
