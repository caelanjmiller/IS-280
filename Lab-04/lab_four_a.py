print("Task 1: String Slicing")
quote: str = "Learning Python is fun!"
print(quote[9:15])
print(quote[-3:])
print()

print("Task 2: Advanced String Formatting")
language: str = "Python"
version: float = 3.8
message: str = "Learning {} {} is fun!".format(language, version)
print(message)
print()

print("Task 3: String Methods")
messyString: str = " Python 3.8 "
cleanedString: str = messyString.strip()
uppercaseString: str = cleanedString.upper()
finalString: str = uppercaseString.replace("3.8", "3.9")
print(finalString)
print()

print("Task 4: Splitting and Joining Strings")
sentences: str = "Python is powerful. Python is easy to learn. Python is open."
sentenceList: list = sentences.split(". ")
# Appears redundant given .split() returns a list
sentenceList: list = [sentence for sentence in sentenceList if sentence]
joinedSentences: str = "||".join(sentenceList)
print(joinedSentences)