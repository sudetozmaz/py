import random
import string
import sys

f = open('codes.txt','w')

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

print ("Generating a Random String including letters and digits")
while True:
    print (randomStringDigits(8))


message = f.write()
print(message)
f.close()