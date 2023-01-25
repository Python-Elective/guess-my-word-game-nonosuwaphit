
import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
      if letter in letters_guessed:
        pass
      else:
        return False
    return True


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    full_word = ''
    for letter in secret_word:
      if letter in letters_guessed:
        full_word += letter
      else:
        full_word += "_"
    return letters_guessed
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...   
    available_letter = string.ascii_lowercase

    for letter in letters_guessed:
        available_letter = available_letter.replace(letter, "")
    return available_letter


#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Let the game begin!")
    print("I am thinking of a word with " + str(len(secret_word))  + "letters")
    guess_num = 8
    guess_list = []
    
    while is_word_guessed(secret_word, guess_list) == False and guess_num > 0:
        print("You have", guess_num, "guesses remaining")
        print("Letters available to you:", get_available_letters(guess_list))
        guess_a_letter = input("Guess a letter:").lower()

        if (guess_a_letter in get_available_letters(guess_list)):
            guess_list.append(guess_a_letter)
            if (guess_a_letter in secret_word):
                print("Correct:", get_guessed_word(secret_word, guess_list))
            else:
                print("Incorrect, this letter is not in my word:", get_guessed_word(secret_word, guess_list))
                guess_num -= 1
        else:
          print("You fool", get_guessed_word(secret_word, guess_list))

    if (is_word_guessed(secret_word, guess_list)):
          print ("You WIN")
    else :
          print("GAME OVER ! The word was",(secret_word))







def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()