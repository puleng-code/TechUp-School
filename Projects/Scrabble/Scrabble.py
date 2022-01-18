letters = {1:['A','E','I','O','U','L','N','R','S','T'],
2:['D','G'],
3:['B','C','M','P'],
4:['F','H','V','W','Y'],
5:['K'],
8:['J','X'],
10:['Q','Z']}
word = input("Please enter your word: ")
print(word)
letter_s = []

#this loop looks uses the word given by the user, then checks if that word exist 
# in the list of letters 
def display(word): # pass in the word that the user inputs as an argument to the function
    scrabble_total = 0 # we will increment this total to track the total for the word
    for letter in word: # loop over the WORD so that you can look at each letter in the word that the user inputted.
        # You're now going to need to loop over the letter dictionary to find the number value for that letter
        for key in letters: # loops over letters dictionary
            if letter in letters[key]: # if the letter in our inputted WORD is in the dictionary
                  print("Letter found!")
                  print("Scrabble letter value is" + key)

display(word)