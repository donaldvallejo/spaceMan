import random

def load_word():
    
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters not in letters_guessed:
            return False

    return True
    

def get_guessed_word(secret_word, letters_guessed):
    blanks = ''
    for letter in secret_word:
        if letter in letters_guessed:
            blanks += letter 
        else: 
            blanks += '_'
    return blanks

    


def is_guess_in_word(guess, secret_word):
    return guess in secret_word
   
def letter_guess():
    guess = ''
    while len(guess) == 0:
        guess = input('Guess a letter: ')

    return guess

def check_used_letters(used_letters):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    nonused_letters = ''
    for letter in letters:
        if letter not in used_letters:
            nonused_letters += letter

    print(f"These letters havn't been guessed yet {nonused_letters}") 

def spaceman(secret_word):
    used_letters = []
    correct_letters = []
    guessesRemaining = 7 
    while guessesRemaining > 0:
        guess = letter_guess()

        if guess not in used_letters:
            used_letters.append(guess)

        if is_guess_in_word(guess, secret_word):
            correct_letters.append(guess)
            blanks = get_guessed_word(secret_word, correct_letters)
            if blanks == secret_word: 
                print(f'You guessed {blanks} correctly you WIN!!!')
                return
            print(f'Guessed word so far {blanks}')

        else:
            guessesRemaining -= 1
            if guessesRemaining == 0:
                print(f'You have 0 guesses remaining you lose. the word was {secret_word}!!!!')
                return
            print('Sorry, your guess was not in the word, try again!')
            print(f'You have {guessesRemaining} incorrect guesses left')
            blanks = get_guessed_word(secret_word, correct_letters)
            print(f'Guessed word so far {blanks}')
        check_used_letters(used_letters)

#These function calls that will start the game
secret_word = load_word()
print(secret_word)
spaceman(secret_word)