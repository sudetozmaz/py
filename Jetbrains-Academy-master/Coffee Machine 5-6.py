# Current/Start Coffee Machine Storage
machineMoney = 550
machineWater = 400
machineMilk = 540
machineBeans = 120
machineCups = 9
power = True

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
    print("${} of money".format(machineMoney))

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

    userCoffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))

    if userCoffee == 1:
        if machineWater >= 250 and machineBeans >= 16 and machineCups >= 1:
            espresso()
            print("I have enough resources, making you a coffee!")
        else:
            if machineWater < 250:
                print("Sorry, not enough water!")
            elif machineBeans < 16:
                print("Sorry, not enough coffee beans!")
            else:
                if machineCups == 0:
                    print("Sorry, not enough cups!")



    elif userCoffee == 2:
        if machineWater >= 350 and machineBeans >= 20 and machineCups >= 1 and machineMilk >= 75:
            latte()
            print("I have enough resources, making you a coffee!")
        else:
            if machineWater < 350:
                print("Sorry, not enough water!")
            elif machineBeans < 20:
                print("Sorry, not enough coffee beans!")
            elif machineMilk < 75:
                print("Sorry, not enough milk!")
            else:
                if machineCups == 0:
                    print("Sorry, not enough cups!")

    else:
        if userCoffee == 3:
            if machineWater >= 200 and machineMilk >= 100 and machineBeans >= 12 and machineCups >= 1:
                cappucino()
                print("I have enough resources, making you a coffee!")
            else:
                if machineWater < 200:
                    print("Sorry, not enough water!")
                elif machineMilk < 100:
                    print("Sorry, not enough milk!")
                elif machineBeans < 12:
                    print("Sorry, not enough coffee beans!")
                else:
                    if machineCups == 0:
                        print("Sorry, not enough cups!")




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



# "Take" function
def take():
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater

    print("I gave you ${}".format(machineMoney))
    machineMoney -= machineMoney

def power():
    global power
    power = False


def ask():
    global answerInput
    global machineBeans
    global machineCups
    global machineMilk
    global machineMoney
    global machineWater
    global power



    print("\n")
    answerInput = input("Write action (buy, fill, take, remaining, exit):")

    if answerInput.lower() == "fill":
        fill()
    elif answerInput.lower() == "buy":
        buy()
    elif answerInput.lower() == "remaining":
        machineDescription()
    elif answerInput.lower() == "exit":
            power()
    else:
        if answerInput.lower() == "take":
            take()

while power:
    ask()