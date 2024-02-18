import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                
cards = [11, 2, 3, 4 ,5 ,6,7,8,9,10,10,10,10]
A_list = []
C_list = []
def new_card():
    player_new_card = random.choice(cards)
    A_list.append(player_new_card)
    com_new_card = random.choice(cards)
    C_list.append(com_new_card)

def score(cards):
    sum = 0
    for n in range(len(cards)):
        sum += cards[n]
    if sum == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum > 21:
        cards.remove(11)
        cards.append(1)
        score(cards)
    return sum


def sum_checker():
    
    close_a = score(A_list) - 21
    close_c = score(C_list) - 21
    if close_a < 0:
        close_a *= -1
        
    if close_c < 0:
        close_c *= -1
    scoreA = score(A_list)
    scoreC = score(C_list)
    if scoreA > 21 :
        print("You went over! So you lose!")
    elif scoreA == 0:
        print("Blackjack! You won.")
    elif close_a > close_c :
        print("You lose!")
    elif close_a < close_c:
        print("you won!")
    elif close_a == close_c:
        print("The game's Draw!")
    

def Blackjack_Capstone_game():
    os.system('cls')
    
    print(logo)
    keep_playing = True
    while keep_playing:
        for n in range(0,2):
            new_card()
        print(f"Your cards are: {A_list} with current score: {score(A_list)}")
        print(f"Computer first card is {C_list[0]}")
        new = input("Type 'y' to add a new card or 'n' to pass!\n")
        if new == 'y':
            new_card()
            score(A_list)
            print(f"Your cards are : {A_list}. current score: {score(A_list)}")
            print(f"Computer first card is {C_list[0]}")
        elif new != 'n':
            print("Invalid input!")
        print(f"Your final hand {A_list}. final score: {score(A_list)}")
        print(f"Computer final hand: {C_list}. Final score: {score(C_list)}")
        sum_checker()
        ask = input("Do you want to play again? Y or N:\nEnter: ").lower()
        if ask == 'y':
            A_list.clear()
            C_list.clear()
        else:
            print("Thanks for playing!")
            keep_playing = False
            


ask = input("Do you want to play Blackjack Capstone Game: Y or n\nEnter: ").lower()
if ask == 'y':
    Blackjack_Capstone_game()
elif ask != 'n':
    print("Invalid input! Program exited...")
