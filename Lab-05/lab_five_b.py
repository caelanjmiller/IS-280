print("Task 1: Writing to a File")
quote: str = input("What's your favorite quote? ")
author: str = input("Who's the author of the quote? ")

with open('favorite_quote.txt', 'w') as file:
    file.write(f"{quote} - {author}\n")
print("Your favorite quote has been saved to favorite_quote.txt.")
print()

print("Task 2: Reading from a File")
with open('favorite_quote.txt', 'r') as file:
    content = file.read()
print("Your favorite quote is:")
print(content)

print("Task 3: Appending to a File")
quote = input("What's another favorite quote of yours? ")
author = input("Who's the author of this quote? ")
with open('favorite_quote.txt', 'a') as file:
    file.write(f"{quote} - {author}\n")
print("Your additional favorite quote has been saved to favorite_quote.txt.")
print()

print("Task 4: Reading Each Line from a File")
with open('favorite_quote.txt', 'r') as file:
    lines = file.readlines()
    print("Your favorite quotes are:")
    line_number = 1
    for line in lines:
        cleaned_line = line.strip()
        print(str(line_number) + (". ") + cleaned_line)
        line_number += 1
print()

print("Task 5: Counting Words from a File")
with open('favorite_quote.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
print(f"The total number of words in your favorite quotes is: {word_count}")