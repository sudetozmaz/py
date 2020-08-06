import math

waterInput = int(input("Write how many ml of water the coffee machine has:"))
milkInput = int(input("Write how many ml of milk the coffee machine has:"))
coffeeBeansInput = int(input("Write how many grams of coffee beans the coffee machine has:"))
cupsOfCoffeeInput = int(input("Write how many cups of coffee you will need:"))

neededWater = cupsOfCoffeeInput * 200
neededMilk = cupsOfCoffeeInput * 50
neededCoffeeBeans = cupsOfCoffeeInput * 15

maxWater = 0
maxMilk = 0
maxBeans = 0

maxWater = math.floor(waterInput / 200)
maxMilk = math.floor(milkInput / 50)
maxBeans = math.floor(coffeeBeansInput / 15)

theMaxPossible = min(maxBeans, maxMilk, maxWater)

if waterInput >= neededWater:
    if milkInput >= neededMilk:
        if coffeeBeansInput >= neededCoffeeBeans:
            if theMaxPossible > cupsOfCoffeeInput:
                print("Yes, I can make that amount of coffee (and even {} more than that)".format(theMaxPossible - int(cupsOfCoffeeInput)))
            else:
                print("Yes, I can make that amount of coffee")

else:
    if theMaxPossible > 0:
        print("No, I can make only {} cups of coffee".format(theMaxPossible))
    else:
        print("No, I can make only 0 cups of coffee")