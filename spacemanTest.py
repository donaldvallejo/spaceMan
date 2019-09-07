import random 

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    # f = open('words.txt', 'r')
    # words_list = f.readlines()
    # test = words_list.split(' ')
    # f.close()
    # print(random.choice(test))

    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters not in letters_guessed:
            return False

    return True

secret_word = load_word()
print(secret_word)
# spaceman(secret_word)