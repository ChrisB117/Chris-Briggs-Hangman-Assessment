#Hangman assessment, (91373)
#Christopher Briggs

#Importing required functions
import random

#Setting the list of words
WORDLIST = ["Abyss", "Awkward", "Avenue", "Bagpipes", "Banjo", "Croquet", "Church", "Crypt", "Dwarves", "Elephant", "Fuzzy", "Gazebo", "Glyph", "Gypsy", "Hangman", "Hyphen", "Ivory", "Jinx", "Jazz", "Jukebox", "Kayak", "Kiosk", "Latte", "Lazy", "Muffin", "Nugget", "Oxygen", "Pixel", "Quad", "Quiz", "Rogue", "Swivel", "Twelfth", "Unified", "Vigorous", "Wildebeest", "Xylophone", "Yacht", "Yak", "Zigzagging"]

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
    if gameLength <= 40 and gameLength >= 1:
        quit
    else:
        int(input("Please choose a number between 1 & 40 "))

#WORDGUESS Function
#The main function that makes it all work
def WORDGUESS():
    word = random.choice(WORDLIST)
    print(word)
    print(len(word))

http://stackoverflow.com/questions/33890590/how-to-replace-the-underscores-with-chosen-letters-in-hangman
http://stackoverflow.com/questions/32960141/how-can-i-replace-the-letters-of-a-string-with-underscores

#####Main Routine#####     
length()

while gameLength < 0:
    quit
else:
    WORDGUESS()

print("Thanks for playing! You have played all your games.")


