import random
from words_list import words
import string

lives = 10

def get_valid_word(words):
    word = random.choice(words) #randomly choosing a word from our list.
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #the letters in the word chosen
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # the letters already guessed

#get that user input!
    user_letter = input('Try a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives = lives -1                #got letter wrong so minus a life!
            print('Oh no! That was incorrect, you have lost a life. New life total is', lives)
    elif user_letter in used_letters:
        print('This is one you have guessed before, try again.')
