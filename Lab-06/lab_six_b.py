import math_tools

def main():
    a: float = float(input("Enter the first number: "))
    b: float = float(input("Enter the second number: "))
    print()
    print(f"Results")
    print(f"Added: {math_tools.add(a, b)}")
    print(f"Subtracted: {math_tools.subtract(a,b)}")
    print(f"Multiplied: {math_tools.multiply(a,b)}")
    print(f"Divided: {math_tools.divide(a,b):.2f}")


if __name__ == "__main__":
    main()