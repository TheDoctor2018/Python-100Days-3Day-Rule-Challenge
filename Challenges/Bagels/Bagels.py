
#Bagels
#Mission
    #User enters 3 digit input.
    #Users has x amount of tries.
    #If correct number in wrong place, return "Pico"
    #If correct number in the right place, return "Fermi"
    #If the correct numbers are all in the right place, return "Bagels"

BagelCode = [3, 4, 5] #3 Digit number.
TryCounter = 10 
Guess = False
Pico = 'Pico'
Fermi = 'Fermi'
Bagels = 'Bagels'

print("Bage;s, a deductive logic game.")
print("I am thinking of a 3 digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I sa: That means")
print(" Pico        One Digit is correct but in the wrong position.")
print(" Farmi       One Digit is correct but in the right position.")
print(" Bagels      No digit is correct.")
print(" I have tought of a number, and you have 10 guesses to get it.")

#Later can add random for generating random Bagel Code

while Guess == False:
    print("Guess: " + str(TryCounter))

    print("Enter 3digit guess")

    PlayerInput = input() #User should only be able to enter 3 digits
    #Convert player input to array
    PlayerInput = list(map(int, str(PlayerInput)))
   #print(PlayerInput)#Test
   #print(BagelCode) #Test
    
   #Convert and compare array values from player to BagelCode
   #Recreate as Function later.!

    #All Digits Wrong
    if (BagelCode[0] != PlayerInput[0]) and (BagelCode[1] != PlayerInput[1]) and (BagelCode[2] != PlayerInput[2]): #Works but needs to be done better with for loop later
        print("Bagels")
        TryCounter = TryCounter -1 #Counter Goes Down
    #All Digits Correct
    if (BagelCode[0] == PlayerInput[0]) and (BagelCode[1] == PlayerInput[1]) and (BagelCode[2] == PlayerInput[2]): #Works but needs to be done better with for loop later
        print("You got it!")
        print("Do you want to play again? (y or n)")
        PlayerDecision = input()
        if PlayerDecision == 'y':
            TryCounter == 10
        else:
            print("Thank you for playing.")
            Guess == True
            exit() #/

    for i in range(len(PlayerInput)):
        if PlayerInput[i] == BagelCode[i]:
            print("Fermi")
        elif PlayerInput[i] in BagelCode:
            print("Pico")
            





