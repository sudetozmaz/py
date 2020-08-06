# Write your code here
from random import randint

# Intro

print("H A N G M A N")
print("The game will be available soon.")

# BOT Section

possibleWords = ["python","java","kotlin","javascript"]
randomChoose = randint(0,3)
chosenWord = "python"


if randomChoose == 0:
    chosenWord = possibleWords[0]
elif randomChoose == 1:
    chosenWord = possibleWords[1]
elif randomChoose == 2:
    chosenWord = possibleWords[2]
else:
    if randomChoose == 3:
        chosenWord = possibleWords[3]

firstThree = chosenWord[:3]
dashAmount = len(chosenWord) - 3

# User section
userInput = input("Guess the word {}{}: ".format(firstThree, "-"*dashAmount))

if userInput.lower() == chosenWord:
    print("You survived!")
else:
    print("You are hanged!")