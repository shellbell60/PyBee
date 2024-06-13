#import the following modules: time, random and re.

import time
import random
import re


FILE_NAME = 'SpellingBee.txt'   #Text file that contains all words in the dictionary. 


'This code is a game similar to the NYT Spelling Bee game. Users will be presented with 7 letters.'
'They will have two minutes to make as many words as possible with the 7 letters. Words must be a '
'minimum of 4 characters and letters may be used more than once. Words will be checked against a'
'dictionary. Users are encouraged to find the Pygram - a word which uses all seven lettters.'
'There may be more than one word that uses all 7 letters but to get the Pygram, the user must find'
'the correct word. If a user chooses to finish before time is up, they can type "EXIT".'


def main():
    
    # creates variables used in the timer function.
    now = time.time()
    future = now + 120

    # open text file that contains word dictionary. It is read into a Python list called 'content'
    with open('SpellingBee.txt', 'r') as file:
        content = file.read()

    # Welcome Screen      
    welcome_screen()

    #Game rules
    game_rules()

    # creates empty lists for randmom letters to be guessed
    letters = []


    # Opens a text file that contains Pygrams (a special word that uses each guessed letter one time)
    # The random function is used to pick a random scrambled Pygram with each game. This word is appended to the
    # letters list. These letters are presented to the user with each turn.

    with open("PangramSearch.txt", "r") as file:
        pygram = file.read()
        pygram = [s.strip() for s in pygram.split(",")]
        random_integer = random.randint(0, 140)
        letters.append(pygram)
        letters = pygram[random_integer]
        print(" ".join(letters))   
        print("")

    with open("PangramFinal.txt", "r") as file:
        pygrams_final = file.read()

    # creased empty guessed words list and fills it with input from user.
    guessed_words = []

    while True:
        
        # a timer is set which starts running when the user is prompted for their first word.
        future = now + 120
        if time.time() > future: # When time is up, user receives a "TIME'S UP message"
            print("TIME'S UP!!!!")
            print("")
            print("")
            break
        
        #while the timer is running, the rest of the game code runs.
        else:       
            allowed_letters = ("'" + letters + "'") #formats a variable so that function will recognize allowed letters
            input_str = input("Please enter a word. Type EXIT to end program: ") #prompts user for input
            print("")
            check_input(input_str)  # functio that checks length of input string

            if input_str == "EXIT":  #condition if user types EXIT before time is up.
                final_score = len(guessed_words) # calculates a final score for user based on length of guessed words list.
                print("Game Over!")
                print("")
                print("You found " +  str(final_score) + " words!") #Tells user how many words they found.
                print("")
                print("Thanks for playing:")
                print("")
                print("")
                #welcome_screen()
                break
            
            # calls function that checks user is only using the assigned letters.
            check_allowed_letters(allowed_letters, input_str)
            
            #checks that user input exists in the dictionary.
            if input_str not in content:
                print("Invalid word")
                print("")
            
            #checks for duplicate words
            elif input_str in guessed_words:
                print("You already entered that word.")
                print("")
            
            # checks if user_input is a Pygram. Must be in content and also in list of Pygrams.
            # displays message announcing Pygram
            elif input_str in content:
                if input_str in pygrams_final and len(input_str) == 7:
                    print("")
                    print("")
                    print("")
                    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
                    print('>>%-2s<<' %('   PyGram!'),'>>%-2s<<' %('BEE'))
                    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))

                #when all conditions are met, user input is appended to the guessed_words list.
                if input_str != "":
                    if re.match('^[{}]+$'.format(allowed_letters), input_str):
                        if len(input_str) > 3:
                            print("")
                            guessed_words.append(input_str)
                            print(' '.join(letters))
                            print("")
                            print(', '.join(guessed_words))
                            print("")

# function that checkes that user is only inputting allowed letters.
def check_allowed_letters(allowed_letters, input_str):
    if not re.match('^[{}]+$'.format(allowed_letters), input_str):
        print("")
        print("Error! Only letters {} are allowed.".format(allowed_letters))
        print("")          

# function that checks length of user input.
def check_input(input_str):
    if len(input_str) < 4:
        print("Words must be at least 4 letters")
        print("")                    

# presents the rules of the game.
def game_rules():
    print('')
    print('')
    print('You will be presented with 7 random letters. Make as many words as you can before time is up!')
    print('Minimum word length is 4 characters and you can use letters more than one time.')
    print('Try to find the special Pygram (a word that uses all the letters 1 time.)')
    print('')
    print('')

# Welcome screen
def welcome_screen():
    print('')
    print('')
    print('')
    print('>><<','>><<','>><<','>><<')
    print('>><<','>><<','>><<','>><<')
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>>%-2s<<' %('Py        '),'>>%-2s<<' %('BEE'))
    print('>><<','>><<','>><<','>><<')
    print('>><<','>><<','>><<','>><<')
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))
    print('>>%-2s<<' %('Py'))


#clears terminal
def clear_terminal():
    for i in range(20):
      print('\n')    
    



if __name__ == '__main__':
    main()