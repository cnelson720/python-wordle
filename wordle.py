import random

words = set()

with open('words', 'r') as file:
    for line in file:
        words.add(line.strip())

attempt_counter = 1

# 00102 (output) 0 = not in word, 1 = in word, wrong place, 2 = right letter, right place

def word_checker(user_guess, word):
    code = ''

    for i, letter in enumerate(user_guess):
        if letter == word[i]:
            # exact letter match (2)
            code += '2'
        elif letter in word:
            # letter is in the word just wrong place
            code += '1'
        else:
            # no matches
            code += '0'

    return code


word_to_guess = random.choice(list(words))
print(word_to_guess)

guessed_words = set()

print('Welcome to Python wordle.')
print('How to play:\nYou get 6 attempts to guess the word. It must be a real word and be 5 letters. Once you make your first guess\n'
          'you will receive a coded hint. The code is a number for each letter you guessed.\n0 means the letter is not in the word at all. 1 '
          'means the letter is in the word, its just in the wrong place. 2 means its the right letter AND the right place. Good luck!')

while attempt_counter < 7:
    print(f"You are on attempt {attempt_counter}/6")

    attempt = input('Enter your guess: ')

    # check if guess is 5 letters OR is a word in the word set OR already guessed
    while len(attempt) != 5 or attempt not in words or attempt in guessed_words:
        attempt = input('Try again: ')

    if attempt == word_to_guess:
        print(f'You guessed it!\nThe word was {word_to_guess}')
        break

    guessed_words.add(attempt)
    response = word_checker(attempt, word_to_guess)
    attempt_counter += 1

    print(response)


if attempt_counter > 6:
    print(f"You lose. The word was {word_to_guess}")
