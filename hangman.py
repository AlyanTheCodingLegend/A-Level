# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    temp=""
    for i in range(len(letters_guessed)):
      temp=temp+letters_guessed[i]
    temp=sorted(temp)
    temp2=sorted(secret_word)  
    if temp==temp2:
      return True
    else:
      return False   




def get_guessed_word(secret_word, letters_guessed):
    return_str=""
    for i in range(len(secret_word)):
        temp=False
        for j in range(len(letters_guessed)):
            if secret_word[i]==letters_guessed[j]:
                temp=True
                return_str=return_str+letters_guessed[j]
        if temp==False:
            return_str=return_str+"_ "
    return return_str            

def get_unique_letters(secret_word):
    temp=secret_word
    unique_letters=len(secret_word)
    while len(temp)>0:
        letter=temp[0]
        same_letter=temp.count(letter)
        unique_letters=unique_letters-(same_letter-1)
        temp=temp.replace(letter,"")
    return unique_letters


def get_available_letters(letters_guessed):
    return_str="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(letters_guessed)):
        return_str.replace(letters_guessed[i],"")
    return return_str
    

def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    guesses=6
    letters_guessed=[]

    unique_letters=get_unique_letters(secret_word)

    while guesses!=0 and is_word_guessed(secret_word,letters_guessed)==False:
      temp=False
      warnings_remaining=3
      print("------------")
      print(f"You have {guesses} guesses left.")
      print(get_available_letters(letters_guessed))
      user_inp=input("Please guess a letter: ").lower()
      while len(user_inp)!=1 and not(ord(user_inp)>=97 and ord(user_inp)<=122):
        user_inp=input("Please guess a letter: ").lower()
        if len(user_inp)!=1 and not((ord(user_inp)>=97 and ord(user_inp)<=122)):
            warnings_remaining-=1
            print(f"The amount of remaining warnings are: {warnings_remaining}")
        if warnings_remaining<=0:
            guesses-=1    
            
      letters_guessed.append(user_inp)
      for i in range(len(secret_word)):
          if secret_word[i]==user_inp:
              temp=True
      if temp==True:
          print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")        
      else:
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}")
          guesses-=1
    if guesses==0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    else:
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {guesses*unique_letters}")

                





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman(secret_word)
     

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

   