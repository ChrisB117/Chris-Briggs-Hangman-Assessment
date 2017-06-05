#Hangman assessment, (91373)
#Christopher Briggs

#Importing required functions
import random
import time
#Setting the list of words
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]

##TESTING##
#i = -1
#while i < 40:
#    i = i + 1
#    print(WORDLIST[i])
##TESTING##

#Asking user for the length of game they want to play
guesses = ''
#WORDGUESS Function
#The main function that makes it all work
def WORDGUESS():
    guesses = ''
    gameLength = int(input("How many words do you want to play? You can chose anywhere from 1-40: ")
    if gameLength <= 40 and gameLength >= 1:
        quit
    else:
        int(input("Please choose a number between 1 & 40 "))
    wordguess = random.choice(WORDLIST)
    while gameLength <= 0:
        break
    else:
        turns = 10
        while turns > 0:         
            failed = 0             
            for letter in wordguess:      
                if letter in guesses:
                    print(letter),
                else:
                    #Displays a dash where a letter is yet to be guessed
                    print("_"),     
                    failed += 1
            if failed == 0:        
                print("You won")
                break
            print()
            guess = input("guess a letter: ")
            guesses += guess
            if guess not in WORDLIST:  
                turns -= 1
                print("You have", + turns, 'more guesses')
                if turns <= 0:           
                    print("You Loose")
                    gameLength -= 1
                    print(wordguess)

                
#####Main Routine#####     
while gameLength <= 0:
    quit()
else:
    WORDGUESS()

print("Thanks for playing! You have played all your games.")


