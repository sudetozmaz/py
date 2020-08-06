#Simple Rock, Paper, Scissors made for Jetbrains Cirriculum
#
#After running the .py extension file in the directory. By typing
#
#"rock"
#"paper"
#"scissors"
#any of the commands above, you can start/finish the game!


from random import randint

userInput = input()

computerChoice = "rock"

possibleChoices = ['rock','paper','scissors']
theChoice = randint(0,2)

if theChoice == 0:
    computerChoice = 'rock'
elif theChoice == 1:
    computerChoice = "paper"
else:
    if theChoice == 2:
        computerChoice == "scissors"


if userInput == computerChoice:
    print("There is a draw", computerChoice)


# Rock input comparison

elif userInput.lower() == "rock":
    if computerChoice == "paper":
        print("Sorry, but computer chose", computerChoice)
    else:
        if computerChoice == "scissors":
            print("Well done. Computer chose", computerChoice, "and failed")

# Paper input comparison
elif userInput.lower() == "paper":
    if computerChoice == "scissors":
        print("Sorry, but computer chose", computerChoice)
    else:
        if computerChoice == "rock":
            print("Well done. Computer chose", computerChoice, "and failed")

# Scissors input comparison
elif userInput.lower() == "scissors":
    if computerChoice == "rock":
        print("Sorry, but computer chose", computerChoice)
    else:
        if computerChoice == "paper":
            print("Well done. Computer chose", computerChoice, "and failed")
