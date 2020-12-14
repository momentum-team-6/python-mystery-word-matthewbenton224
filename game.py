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

e_words = []
m_words = []
h_words = []
d_words = []

for word in u_list:
    if len(word) >= 3 and len(word) <= 5:
        e_words.append(word)
    if len(word) >= 6 and len(word) <= 8:
        m_words.append(word)
    if len(word) >= 9 and len(word) <= 12:
        h_words.append(word)
    if len(word) >= 13 and len(word) <= 25:
        d_words.append(word)

while True:
    difficulty = input("A Game is afoot. Choose your adventure level: Easy, Medium, Hard, Demon ")
    if difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard" and difficulty != "Demon":
        continue
    else:
        break

a_list = None
if difficulty == "Easy":
    a_list = e_words
elif difficulty == "Medium":
    a_list = m_words
elif difficulty == "Hard":
    a_list = h_words
elif difficulty == "Demon":
    a_list = d_words

import random
c_word = random.choice(a_list)
c_word_list = [letter for letter in c_word]
print('computer word is: ', c_word)

display_word = ['_' for letter in range(len(c_word))]
print(" ".join(display_word))

positions = []
max_guesses = 8
tries = 0
memory = []

while c_word_list != display_word and max_guesses > 0:
   guess = input('Guess A Letter: ')
   u_guess = guess.upper()


   if u_guess == "":
        print("Guess A Letter")
   elif u_guess in memory:
        print(f"YO! Pay Attention, {u_guess} has already been tried")
   elif u_guess in c_word_list:
        memory.append(u_guess)
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
