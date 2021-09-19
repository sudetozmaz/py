#import this

#name = "     vusal ismayilov celebi      "


# basic string manipulations:
    print(name.title())
    print(name.upper())
    print(name.lower())


# string formatting:
    print("Vusal\nIsmayilov")
    print("Vusal\tIsmayilov")


# cleaning the strings:
    print(name.rstrip()) # strip whitespaces from the right side
    print(name.lstrip()) # strip whitespaces from the left side
    print(name.strip()) # strip the whitespaces from both sides


# a custom list:
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles[0].title())


motorcycles = ['honda', 'yamaha', 'suzuki']
# adding/appending values to the list
    motorcycles.append("last element") # append element to the last
    motorcycles.insert(0, "first element") # insert element to the first
                                            # index


# deleting/removing elements from the list
    del motorcycles[0] # delete the element with the index
    motorcycles.pop() # remove the last element of the list
                       from the original list, and return
                       the removed element as return
    motorcycles.pop(0) # remove the element indexed at 0
                        from the list called motorcycles
                        and return the removed element
    motorcyles.remove("honda") # removes the first honda value from 
                                # the list


# sorting a list
    cars = ['bmw', 'audi', 'toyota', 'subaru']

    # direct sorting, inplace=True:
    cars.sort()
    print(cars)

    # reverse sorting, inplace=True:
    cars.sort(reverse=True)
    print(cars)

    # sorting the copy of a list temporarily, inplace=False
    print(cars)
    print(sorted(cars))
    print(cars)


# reversing a list
    # direct reversing, inplace=True:
    cars.reverse()

    # inplace=False reversing:
    cars[::-1]

    # length of a list
    len(cars)


# range and list creations
    random_list = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
    
    numbers = list(range(1,6)) # [1,2,3,4,5]
    even_n = list(range(1,11,2)) # [2,4,6,8,10]
    
    min(random_list) # 1
    max(random_list) # 10
    sum(random_list) # 55


# list comprehensions
    # converting the below code to list comp:
        even_numbers = [] 
        for i in range(11):
           if i % 2 == 0:
               even_numbes.append(i)
        print(even_numbers) # [0,2,4,6,8,10]
        
        # one line even numbers list using lc
        even_numbers = [i for i in range(11) if i % 2 ==  0] # [0,2,4,6,8,10]
                        
# slicing
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    players[0:3] # ['charles', 'martina', 'michael'] 
    
    players[:] # ['charles', 'martina', 'michael', 'florence', 'eli']
    
    players[3:] # ['florence', 'eli']


# copying the list
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friends_food = my_foods # THIS IS NOT COPYING! THIS IS ASSIGNING!

    # proper ways to copy a list:
    #     1) friends_food = my_foods[:]
    #     2) friends_food = my_foods.copy()


# conditions
    car = 'audi'
    car == 'bmw' # False
    car == 'audi' # True

    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    'mushrooms' in requested_toppings # True

# dictionaries
    user = {
        "username":"woosal",
        "first_name":"Vusal",
        "last_name":"Ismayilov"
    }
    
    for key, value in user.items():
        print(key, value)
            #"username":"woosal",
            #"first_name":"Vusal",
            #"last_name":"Ismayilov"
    
    # keys:
        user.keys()

    # values:
        user.values()


# loops
   current number = 0
   while current_number < 10:
      current_number += 1
        if current_number % 2 == 0:
            continue

       print(current_number)


# i/o
    # reading line-by-line
    with open("file.txt") as f:
        for line in f:
            print(line) # prints all the lines inside a file


    # read all file
    with open("file.txt") as f:
        print(f) # prints all the content inside a file

    # count occurrences in a file
    line = "Row, row, row your boat"
    print(line.count('row')) # 2
    print(line.lower().count('row')) # 3

# json
    import json

    print(json.dumps({'b': 1, 'a': 2}, sort_keys=True, indent=4))

# unittest

    assertEqual(a, b) Verify that a == b
    assertNotEqual(a, b) Verify that a != b
    assertTrue(x) Verify that x is True
    assertFalse(x) Verify that x is False
    assertIn(item, list) Verify that item is in list
    assertNotIn(item, list) Verify that item is not in list
