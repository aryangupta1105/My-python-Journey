from game_data import data
from art import logo,vs
import random
import os
def celeb_choser():
    celeb = random.choice(data)
    return celeb
def display_celeb(celeb):
    return f"{celeb['name']}, a {celeb['description']}, from {celeb['country']}"

def checker(guess,celeb1 ,celeb2):
    if celeb1['follower_count'] > celeb2['follower_count']:
        return guess == 'a'
    elif celeb1['follower_count'] < celeb2['follower_count']:
        return guess == 'b'

def higher_lower():
    score = 0
    print(logo)
    keep_playing = True
    celeb1 = celeb_choser()
    celeb2 = celeb_choser()
    while keep_playing:
        celeb1 = celeb2
        print(f"Compare A: {display_celeb(celeb1)}")
        print(vs)
        celeb2 = celeb_choser()
        print(f"Against B: {display_celeb(celeb2)}")
        guess = input("Who has more followers? type 'A' or 'B'\n ").lower()
        while guess != 'a' and guess != 'b':
            print("Invalid input. Try again!")
            guess = input("Who has more followers? type 'A' or 'B'\n ").lower()
        is_correct = checker(guess,celeb1,celeb2)
        if is_correct:
            score += 1
            print(f"You are correct! Your score: {score}")   
            kneep_playing = True
        else:
            os.system('cls')
            print("Sorry! that's wrong")
            print(f"Final score: {score}")   
            keep_playing = False

higher_lower()
