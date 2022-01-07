
#Variables
wins = 0
loses = 0
ties = 0

import random, sys
print('Rock, Paper, Scissors')
while True:
    print('Enter your move: r(rock), p(paper), s(scissors), or q(quit)')
    playerIput = input()
    if playerIput =='q':
        sys.exit()
    if playerIput =='r' or playerIput =='p'or playerIput =='s':

        break
    print('Type one of r,p,s,or q')

#PLAYER Choices
if playerIput == 'r':
    print('Rock versus')
if playerIput == 'p':
    print('Paper versus')
if playerIput == 's':
    print('Scissors versus')

#Computer Choice
randomnumber = random.randint(1,3)
if randomnumber == 1:
    computermove = 'r'
    print('Rock')

if randomnumber == 2:
    computermove = 'p'
    print('Paper')  

if randomnumber == 3:
    computermove = 's'
    print('Scissors')  

if playerIput == computermove:
    print('Tie')
    ties = ties + 1
elif playerIput == 'r' and computermove =='s':
    print('Win')
    wins = wins + 1
elif playerIput == 'r' and computermove =='p':
    print('looses')
    loses = loses + 1
elif playerIput == 'p' and computermove =='s':
    print('looses')
    loses = loses + 1
elif playerIput == 'p' and computermove =='r':
    print('win')
    wins = wins + 1
elif playerIput == 's' and computermove =='p':
    print('Win')
    wins = wins + 1
elif playerIput == 's' and computermove =='r':
    print('loses')

