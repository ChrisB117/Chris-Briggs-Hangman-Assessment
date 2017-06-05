#Hangman assessment, (91373)
#Christopher Briggs

# importing required functions
import random # allows for a random word to be chosen from the list
import time # adds a delay between display to make the game run smoother

#length Function
# making sure gameLength is between 1 & 40
# and not a string or float
# if number is less than 1 it will be made 1
# if number is more than 40 it will be made 40
def length():
    global gameLength
    try:
        gameLength = int(input("How many games would you like to play? "))
        if gameLength > 40:
            gameLength = 40
            quit
        elif gameLength < 1:
            gameLength = 1
            quit
        else:
            return ValueError
    except ValueError:
         print("Please type a number between 1 and 40 ")
         length()
    return gameLength

#WORDGUESS Function
# the main function that makes it all work
def WORDGUESS():
    global gameLength
    global gamePlayed
    gamePlayed = 0
    guesses = ''
    turns = 10 # setting the number of turns the user is allowed
    word = random.choice(WORDLIST)
    while turns > 0:  # checks if the remaining amount turns is greater than zero
        failed = 0                
        for letter in word:      
            if letter in guesses:  # checks if letter is in the players guess      
                print(letter),  # prints the letter
            else:
                print("_"),  # prints an underscore where a letter is yet to be guessed
                failed += 1    
        if failed == 0:  # if failed equals zero
            print("Congratulations!! You won!")
            gameLength -= 1
            break              
        print()
        guess = input("guess a letter:")  # asks the user to guess a letter
        guess = guess.lower()
        guesses += guess                    
        if guess not in word:
            turns -= 1  # takes away 1 from turns
            print("Wrong")
            time.sleep(0.2)
            print("You have", + turns, 'more guesses')  # displays how many turns the user has left
            if turns == 0:               
                print("You Loose")
                print("The word was " + word)  # prints what the word was
                gameLength -= 1          
    time.sleep(1)
    if gamePlayed == gameLength:
        print()
        print("You've played all your games ")
        quit()

                               
#####Main Routine#####
print("""Welcome to Hangman. You can play a max of 40 games.
In each game you will have 10 guesses to get the word correct""")
time.sleep(6.5)
print()
#Setting the list of words
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]
# calling the length function
length()
# setting gamePlayed to 0
gamePlayed = 0
time.sleep(0.5)

# setting guesses to an empty variable
guesses = ''

# running the main function
while gamePlayed <= gameLength:
    WORDGUESS()
else:
    quit()
