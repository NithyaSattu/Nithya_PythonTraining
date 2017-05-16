"""
19.Play a number guessing game (User enters a guess,
you print YES or Higher or Lower)
"""

import random
randomNumber = random.randrange(0,50)
print "Random number is generated it is from 0 to 50"
guessed = False
while guessed == False:
    userInput = int(input("Your guess please: "))
    if userInput == randomNumber:
        guessed = True
        print "Well done!"
    elif userInput>100:
        print "Our guess range is between 0 and 100, please try a bit lower"
    elif userInput<0:
        print "Our guess range is between 0 and 100, please try a bit higher"
    elif userInput>randomNumber:
        print "Try one more time, a bit lower"
    elif userInput < randomNumber:
        print "Try one more time, a bit higher"

print "End of program"
