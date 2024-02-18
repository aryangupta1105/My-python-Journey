import random
import os
logo = """
    _______               ___.                    ________                            .__                   ________                    _________          
    \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ___\_____   \         
    /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ /   __/         
   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/|   |            
   \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >___|            
           \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/<___>            
    ___                                                                                                                                             ___    
   /  /                                                                                                                                             \  \   
  /  /                                                                                                                                               \  \  
 (  (                                                                                                                                                 )  ) 
  \  \   __________________________________________________________________________________________________________________________________________  /  /  
   \__\ /_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/ /__/   
                                          

"""
def number_guessing_game():
    ''' The number guessing game '''
    print(logo)
    keep_playing = True
    while keep_playing:
        print("I am thinking of a number between 1 and 100.")
        number = random.randint(1,100)
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            lives = 10
        elif difficulty == 'hard':
            lives = 5
        else:
            print("Invalid input!")
        while lives != 0:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if number == guess:
                print(f"You got it! with {lives} attempts left.")
                break
            elif number > guess:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            lives -= 1
        if lives == 0:
            print(f"Sorry you ran out of lives! The correct number was {number}")
        ask = input("Do you want to play again! Y or n: ").lower()
        
        if ask != 'y':
            print("Thanks for playing!")
            keep_playing = False


ask = input("Do you want to play number guessing game: Y or n\n").lower()
if ask == 'y':
    os.system('cls')
    number_guessing_game()
elif ask != 'n':
    print("Invalid input! program exited...")

