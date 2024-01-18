import random


from words import words

import string

def get_valid_word(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hungman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8

    while len(word_letters) > 0 and lives > 0:
        print('you have ', lives ,'lives left and you have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('letter is not in word')

        elif user_letter in used_letters:
            print('you have already used that character ,try again')
        else:
            print('Invalid character')

    if lives == 0:
        print(f'the lives are finished . the word was {word}')

    else:
        print(f'you guessed the word {word} !!')

hungman()