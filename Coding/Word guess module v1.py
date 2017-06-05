# WORDGUESS MODULE v1
# importing requiered functions
import random

# setting the wordlist
WORDLIST = ["abyss", "awkward", "avenue", "bagpipes", "banjo", "croquet", "church", "crypt", "dwarves", "elephant", "fuzzy", "gazebo", "glyph", "gypsy", "hangman", "hyphen", "ivory", "jinx", "jazz", "jukebox", "kayak", "kiosk", "latte", "lazy", "muffin", "nugget", "oxygen", "pixel", "quad", "quiz", "rogue", "swivel", "twelfth", "unified", "vigorous", "wildebeest", "xylophone", "yacht", "yak", "zigzagging"]

###-TESTING-###
i = -1
while i < 40:
    i = i + 1
    print(WORDLIST[i])
###-TESTING-###

# creating variables for guesses and turns
guesses = ''
turns = 10

wordguess = random.choice(WORDLIST)
