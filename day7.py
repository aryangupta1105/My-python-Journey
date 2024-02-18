# Day 7 Hangman Project:-

#task 1:
# import random
# word_list = ['mango','orange','apple']
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter:-  ").lower()
# for letter in chosen_word:
#     if letter == guess:
#         print("matched")
#     else:
#         print("not matched")

# # Day = 6 :
# print("We have studied about Functions on this day using Reeblogs World on google chrome or any other browser:")

#task 2
import random
# from hangman import logo , stages
logo = '''                                                                   
 _ _ _  _____  __     _____  _____  _____  _____    _____  _____   
| | | ||   __||  |   |     ||     ||     ||   __|  |_   _||     |  
| | | ||   __||  |__ |   --||  |  || | | ||   __|    | |  |  |  |  
|_____||_____||_____||_____||_____||_|_|_||_____|    |_|  |_____|  
                                                                     _  | |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
                    ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y/
| |       // |   | \/
| |      //  | O |  \/
| |     ')   |   |   (`
| |          ||l||
| |          || ||
| |          || ||
| |          || ||
| |         / | | |
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . . '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
word_list = ['asshole','bitching','apple']
chosen_word = random.choice(word_list)
# print(f"Psss! The chosen word is {chosen_word}")
print(logo)
# print("Hello User! Welcome to Hangman.")
name = input("What is your name?\n")
age = int(input("Enter your age:- "))
ask = input("Do you want to play Hangman? Y or N\n").lower()
def hangman():
    lives = 6
    display = []
    for letter in chosen_word:
        display += "_"
    print(display)
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter:-  ").lower()
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(0,len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
        print(display)
    
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess} which is not in chosen word. So you lose a life")
            if lives == 0:
                end_of_game = True
                print("you lose")
                
        if "_" not in display:
            end_of_game = True
            print("Yay! You win")
        
        if guess in chosen_word and position != 0 :
                print("Already typed ! same input")
        
        print(stages[lives])
        # clear()
        
if ask == 'y':
    hangman()
elif ask == 'n':
    print("Thanks for joining! Exited...")
else:
    print("Invalid Input!! Exited....")
again = input("Do you want to play again? Y or N\n").lower()
if again == 'y':
    hangman()
elif again == 'n':
    print("Thanks for playing.")
else:
    print("Invalid Input!! Exited..")

    