# Current/Start Coffee Machine Storage
machineMoney = 550
machineWater = 1200
machineMilk = 540
machineBeans = 120
machineCups = 9

# Functions

# Machine Leftover Description
def machineDescription():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    print("")
    print("The coffee mahine has:")
    print("{} of water".format(machineWater))
    print("{} of milk".format(machineMilk))
    print("{} of coffee beans".format(machineBeans))
    print("{} of disposable cups".format(machineCups))
    print("{} of money".format(machineMoney))

# Coffee Types
def espresso():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    machineWater -= 250
    machineBeans -= 16
    machineMoney += 4
    machineCups -= 1


def latte():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    machineWater -= 350
    machineMilk -= 75
    machineBeans -= 20
    machineMoney += 7
    machineCups -= 1


def cappucino():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    machineWater -= 200
    machineMilk -= 100
    machineBeans -= 12
    machineMoney += 6
    machineCups -= 1

# "Buy" function
def buy():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    userCoffee = int(input())

    if userCoffee == 1:
        espresso()
    elif userCoffee == 2:
        latte()
    else:
        if userCoffee == 3:
            cappucino()
        else:
            print("Unfortuantely, we do not have that type of coffee!")

    machineDescription()


# "Fill" function
def fill():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    fillWater = int(input("Write how many ml of water do you want to add:"))
    fillMilk =  int(input("Write how many ml of milk do you want to add:"))
    fillBeans = int(input("Write how many grams of coffee beans do you want to add:"))
    fillCups = int(input("Write how many disposable cups of coffee do you want to add:"))

    machineWater += fillWater
    machineMilk += fillMilk
    machineBeans += fillBeans
    machineCups += fillCups

    machineDescription()

# "Take" function
def take():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    print("I gave you ${}".format(machineMoney))
    machineMoney -= machineMoney
    machineDescription()


def ask():
    global answerInput
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    machineDescription()
    print("\n")
    answerInput = input("Write action (buy, fill, take):")

    if answerInput.lower() == "fill":
        fill()
    elif answerInput.lower() == "buy":
        buy()
    else:
        if answerInput.lower() == "take":
            take()

ask()