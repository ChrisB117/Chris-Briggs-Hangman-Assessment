#Hangman assessment, (91373)
#Christopher Briggs

#Importing required functions
import random #Allows for a random word to be chosen from the list
import time #Adds a delay between display to make the game run smoother
#Setting the list of words
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]

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
    gamePlayed = 0
    guesses = ''
    turns = 10
    wordguess = random.choice(WORDLIST)
    # checks if the remaining amount turns is greater than zero
    while turns > 0:
        failed = 0                
        for letter in wordguess:      
        # checks if letter is in the players guess
            if letter in guesses:        
            # prints the letter
                print(letter),    
            else:
            # prints an underscore where a letter is yet to be guessed
                print("_"),
                failed += 1    
        # if failed equals zero
        if failed == 0:
            gamePlayed + 1
            print("You won")  
            break              
        print()
        # asks the user to guess a character
        guess = input("guess a letter:") 
        guesses += guess                    
        if guess not in wordguess:
         # takes away 1 from turns
            turns -= 1
            print("Wrong")
            time.sleep(0.2)
            # displays how many turns you have left
            print("You have", + turns, 'more guesses') 
            if turns == 0:               
                print("You Loose")
            # prints what the word was
                print("The word was " + wordguess)
                gamePlayed + 1          
    time.sleep(1)
    if gamePlayed == gameLength:
        print("You've played all your games ")
        quit()

                               
#####Main Routine#####     
length()
gamePlayed = 0
time.sleep(0.5)

if gamePlayed < gameLength:
    WORDGUESS()
else:
    quit()

again = input("Would you like to play again? ")
length()
if again == 'yes':
    gamePlayed = 0
    time.sleep(0.5)    
    while gamePlayed == gameLength:
        quit()
    else:
        WORDGUESS() 
elif again == 'no':
    print("Thank you for playing! Come back soon :) ")
    time.sleep(2)
    quit()
quit()
