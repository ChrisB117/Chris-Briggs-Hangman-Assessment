# WORDGUESS MODULE v2
# importing requiered functions
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
    # prints You Won
    if failed == 0:        
        print("You won")  
        break              
    print()
