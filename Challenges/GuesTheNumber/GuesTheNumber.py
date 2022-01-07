
#Goal
#Make a guyess the number code.
#Add Error handling for input thats not an integer.--WIP
    #--Takes the non integer as a value and needs to be fixed.
#Make the code repeat indefinitely only if user chooses.--WIP
#Add a function to clean up.--WIP

#Test Test
#Variables
import random, sys, re
print('I am thinking of a number between 1-20.')
print('Enter a to exit')
print('Take a guess')
randomnumber = random.randint(1,20)

while True:

    
    try: 
        playerIput = int(input())
    except ValueError:
        print('Not an integer')

    if playerIput == randomnumber:
        print(' Good Job, you guess the correct number.')
        print('Would you like to play again? Press Enter else q')
    if playerIput =='q':
        sys.exit()   
    if playerIput  <= 0:
        print('Print an input in the correct range')
        print('Take another guess.')
    elif playerIput  >= 21:
        print('Print an input in the correct range')
        print('Take another guess.')
    elif playerIput  < randomnumber:
        print('Your guess is to low.')
        print('Take another guess.')
    elif playerIput  > randomnumber:
        print('Your guess is to High.')
        print('Take another guess.')