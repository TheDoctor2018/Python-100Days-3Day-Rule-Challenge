#How to create a small zig zag patter animation.



import time,sys
indent = 0 #How many space to indent.
changeup = 0 # how many times the patterns reaches 20 before its changed.
indentIncreasing = True #Whether the indentation is increasing or not. 
Pattern = 'L'


try:
    while True: #The main program loop.
        print(' '*indent, end='')

        print(Pattern,Pattern,Pattern,Pattern,Pattern,Pattern,Pattern,Pattern)

        time.sleep(0.1)#pause for 1/10 of a second

        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent +1
            if indent == 20:

                changeup = changeup +1
                #change the pattern
                if changeup == 2:
                    Pattern = 'M'
                if changeup == 4:
                    Pattern = 'O'
                if changeup == 6:
                    Pattern = 'L'
                    changeup = 0 #resets
                #change direction
                indent = False
                
        else:
            #Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
