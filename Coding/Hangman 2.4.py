#Hangman assessment, (91373)
#Christopher Briggs

# importing required functions
import random # allows for a random word to be chosen from the list
import time # adds a delay between display to make the game run smoother

#length Function
# making sure gameLength is between 1 & 40
def length():
    global gameLength
    if gameLength <= 40 and gameLength >= 1:
        quit
    else:
        int(input("Please choose a number between 1 & 40 "))

#WORDGUESS Function
# the main function that makes it all work
def WORDGUESS():
    global gameLength
    global gamePlayed
    gamePlayed = 0
    guesses = ''
    turns = 10 # setting the number of turns the user is allowed
    wordguess = random.choice(WORDLIST)
    while turns > 0:  # checks if the remaining amount turns is greater than zero
        failed = 0                
        for letter in wordguess:      
            if letter in guesses:  # checks if letter is in the players guess      
                print(letter),  # prints the letter
            else:
                print("_"),  # prints an underscore where a letter is yet to be guessed
                failed += 1    
        if failed == 0:  # if failed equals zero
            gamePlayed + 1
            print("You won")  
            break              
        print()
        guess = input("guess a letter:")  # asks the user to guess a letter
        guesses += guess                    
        if guess not in wordguess:
            turns -= 1  # takes away 1 from turns
            print("Wrong")
            time.sleep(0.2)
            print("You have", + turns, 'more guesses')  # displays how many turns the user has left
            if turns == 0:               
                print("You Loose")
                print("The word was " + wordguess)  # prints what the word was
                gamePlayed + 1          
    time.sleep(1)
    if gamePlayed == gameLength:
        print("You've played all your games ")
        quit()

                               
#####Main Routine#####
#Setting the list of words
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]
# asking user for the length of game they want to play
gameLength = int(input("How many words do you want to play? You can chose anywhere from 1-40: "))
# calling the length function
length()
# setting gamePlayed to 0
gamePlayed = 0
time.sleep(0.5)

# setting guesses to an empty variable
guesses = ''

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
