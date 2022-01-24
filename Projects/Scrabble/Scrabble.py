#dictionary representing the values of the letters to be used from Scrabble words
letters = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1,
            'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

#any random word you can think of
word = input("Please enter your word: ")

#the total we going to use to add all values of the letters used from the word given
total = 0

#for all the letters in the given word, will be used to be assigned a value as on the dictionary
for letter in word.lower():
    word_value = letters[letter]   #every letter in the given word is equalized with its value as on the dictionary
    total = word_value + total     #all the letters from the word given, their values added with the total

#prints the total   
print("Your word", word, "is worth",total,"points","\n")