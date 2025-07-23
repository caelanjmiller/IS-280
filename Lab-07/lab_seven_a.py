class Rectangle():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def perimeter(self):
        return (2 * (self.height)) + (2 * (self.width))

    def area(self):
        return self.height * self.width
    
    def __str__(self):
        asterisk_presentation: list = []

        asterisk_presentation.append("* " * self.width)

        for _ in range(self.height - 2):
            if self.width == 1:
                asterisk_presentation.append("*")
            elif self.width == 2:
                asterisk_presentation.append("* *")
            else:
                asterisk_presentation.append("* " + "  " * (self.width - 2) + "*")
        
        if self.height > 1:
            asterisk_presentation.append("* " * self.width)

        return "\n".join(asterisk_presentation)

def main():
    print(f"Rectangle Calculator")
    continuation: bool = True
    print()
    
    while continuation:
        height: int = int(input("Height: "))
        width: int = int(input("Width: "))
        rectangle: Rectangle = Rectangle(height, width)
        perimeter: int = rectangle.perimeter()
        area: int = rectangle.area()
        print(f"Perimeter: {perimeter}")
        print(f"Area: {area}")
        print(str(rectangle))
        print()
        user_continue: str = input("Continue? (y/n): ")
        if user_continue == 'y':
            continue
        elif user_continue == 'n':
            continuation: bool = False
            print()
        else:
            print({"Invalid command."})

    else:
        print("Bye!")

if __name__ == "__main__":
    main()