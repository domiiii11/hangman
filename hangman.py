'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random
import string
import sys


def check_different_characters(random_word):
    s = set(random_word)
    return len(s)

def fetch_random_word():
    with open('words.txt') as f:
        lines = f.readlines()
        while True:
            random_word = random.choice(lines).strip()
            if len(set(random_word)) <= 6:
                return random_word

def create_empty_word(numbers_of_letters):
    empty_word  = '_'
    for i in range(1, numbers_of_letters):
        empty_word  += " _"
    return empty_word

def collect_used_letters(guessed_letter, used_letters):
    used_letters += ' ' + guessed_letter
    return used_letters

def complement_hidden_word(hidden_word, index, letter):
    index = index * 2
    hidden_word =  hidden_word[:index] + letter +  hidden_word[index + 1:]
    return hidden_word

def check_if_full_word_collected(hidden_word):
    allowed = set(string.ascii_lowercase + ' ')
    word = set(hidden_word)
    if word.issubset(allowed):
        return True
    else:
        return False

def play_again():
    print("Would You like to play again? Type Y or N.") 
    answer = input().lower()
    while answer not in ["y", "n"]:
        print("You typed not Y or N! Answer again.")
        answer = input().lower()
    if answer == "y":
        play_game()
    else:
        sys.exit()

def check_how_much_possible_guesses_left(random_word, hidden_word):
    characters_in_word = check_different_characters(random_word)
    characters_in_hidden_word = check_different_characters(hidden_word) - 2
    characters_dif = characters_in_word - characters_in_hidden_word
    return characters_dif

def play_game():
    random_word = fetch_random_word()
    print(random_word)
    number_of_letters = len(random_word)
    hidden_word = create_empty_word(number_of_letters)
    print("Hi, we will play hangman. You will have 6 guesses. Let's start.")
    used_letters = ''
    for i in range(6):
        print("Guess a letter.")
        guessed_letter = input().lower()
        while not guessed_letter.isalpha():
            print("You typed not a letter! Type again.")
            guessed_letter = input().lower()
        for index, letter in enumerate(random_word):
            if letter == guessed_letter:
                used_letters = collect_used_letters(guessed_letter, used_letters) 
                hidden_word = complement_hidden_word(hidden_word, int(index), guessed_letter)
        print("Used letters: ", used_letters)
        print("Word: ", hidden_word)
        if check_if_full_word_collected(hidden_word):
            print("You guessed the word " + random_word + ". Well done!")
            play_again()
        else:
            tries_left =  6 - i - 1
            if tries_left >= check_how_much_possible_guesses_left(random_word, hidden_word):
                print("You have " + str(tries_left) + " tries left.")
            else:
                print("You have lost! Would You like to play again?")
                play_again()
                

play_game() 





        


        


    







