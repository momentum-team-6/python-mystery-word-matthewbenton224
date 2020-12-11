# gather the words, so i can import import
# split words up into three groups based on word length
# based on what user chooses, will generate a word out of those groups
# set a hidden display word with all letters visible
# set an empty string as the display word (all underscores)
# "simplementation" is steps 9 - 12
# get user input
# if user input is in word, append to display word in the right spot
# if user input not in word, print ("You're wrong")
# when display word equals hidden word, game is won
# incorprate counter to keep track of guesses

file = open('words.txt', 'r')
opened_file = file.read()

u_list = opened_file.upper().split()

import random
c_word = random.choice(u_list)
c_word_list = [letter for letter in c_word]
print('computer word is: ', c_word)

# for word in u_list:
#    if len(word) == 4:
#        print(word)

display_word = ['_' for letter in range(len(c_word))]
print(display_word)

positions = []
max_guesses = 8
tries = 0

while c_word_list != display_word and max_guesses > 0:
   
    guess = input('Guess A Letter: ')
    u_guess = guess.upper()
    print(u_guess)
    if u_guess in c_word_list:

        for i in range(len(display_word)):
            if u_guess == c_word[i]:
                positions.append(i)
                print(f"\U0001F64C Yas! {u_guess} is in this word \U0001F64C")
                for position in positions:
                    display_word[position] = u_guess
                    positions = []
                    print(display_word)
    else:
        max_guesses -= 1
        print(f"\U0001F6A8 Naw, Homie, {u_guess} is not in the word. You have {max_guesses} left \U0001F6A8")
