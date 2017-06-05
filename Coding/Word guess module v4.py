# WORDGUESS MODULE v4
# importing requiered functions
import time
import random

# setting the wordlist
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]

###-TESTING-###
#i = -1
#while i < 40:
#    i = i + 1
#    print(WORDLIST[i])
###-TESTING-###

# creating variables for guesses and turns
guesses = ''
turns = 10

wordguess = random.choice(WORDLIST)

# checks if the remaining amount turns is greater than zero
while turns > 0:         
    failed = 0
    
    for letter in wordguess:      
    # checks if letter is in the players guess
        if letter in guesses:
            turns + 1   
        # prints the letter
            print(letter),    
        else:    
        # prints an underscore where a letter is yet to be guessed
            print("_"),            
            failed += 1    
    # prints victory message
    if failed == 0:        
        print("You won") 
        break              
    print()

 # asks the user go guess a letter
    guess = input("Guess a letter:")
    time.sleep(0.5)
# sets the users guess to guesses
    guesses += guess                    
    if guess not in WORDLIST:
     # takes away 1 from turns
        turns -= 1 
        print("Wrong")
        time.sleep(0.5)
     # displays how many turns you have left
        print("You have", + turns, 'more guesses')   
        if turns == 0:           
     # prints "You Loose"
            print("You Loose")
