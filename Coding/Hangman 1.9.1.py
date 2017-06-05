#Hangman assessment, (91373)
#Christopher Briggs

#Importing required functions
import random #Allows for a random word to be chosen from the list
import time #Adds a delay between display to make the game run smoother
#Setting the list of words
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]

##TESTING##
#i = -1
#while i < 40:
#    i = i + 1
#    print(WORDLIST[i])
##TESTING##

#Asking user for the length of game they want to play
gameLength = int(input("How many words do you want to play? You can chose anywhere from 1-40: "))
#Making sure it's inbetween 1 & 40
def length():
    global gameLength
    if gameLength <= 40 and gameLength >= 1:
        quit
    else:
        int(input("Please choose a number between 1 & 40 "))

guesses = ''
#WORDGUESS Function
#The main function that makes it all work
def WORDGUESS():
    global gameLength
    global gamePlayed
    guesses = ''
    wordguess = random.choice(WORDLIST)
    turns = 10
    while turns > 0:         
        failed = 0             
        for letter in wordguess:      
            if letter in guesses:
                print(letter),
            else:
                #Displays a dash where a letter is yet to be guessed
                print('_'),     
                failed += 1
        if failed == 0:
            gamePlayed += 1
            gameLength -= gamePlayed
            print("You won")
            break
            print()
        guess = input("guess a letter: ")
        guesses += guess
        if guess not in WORDLIST:  
            turns -= 1
            time.sleep(0.33)
            print("You have", + turns, 'more guesses')
        elif turns == 0:
            print("You have no more guesses")
            if turns <= 0:
                print("You Loose")
                print("The word was: " + wordguess)
                gamePlayed += 1
                gameLength -= gamePlayed
    time.sleep(1)
    if gamePlayed == gameLength:
        print("Congratulations!! You've won!")
        quit
    else:
        print()
        print("You Loose")
        print("The word was: " + wordguess)
        time.sleep(1)
        print()
        gamePlayed += 1
        gameLength -= gamePlayed
        print("Here's your next word ")
        time.sleep(1)
        WORDGUESS()
                 

                
#####Main Routine#####     
length()
gamePlayed = 0
time.sleep(0.5)

while gamePlayed == gameLength:
    quit()
else:
    WORDGUESS()

again = input("Would you like to play again? ")
if again == 'yes':
    length()
    gamePlayed = 0
    time.sleep(0.5)
    
    while gamePlayed == gameLength:
        quit()
    else:
        WORDGUESS() 
