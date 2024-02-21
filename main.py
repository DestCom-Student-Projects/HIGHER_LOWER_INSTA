import os
from dotenv import load_dotenv
import instaloader
import random

from celebrity_list import CELEBRITY_LIST

load_dotenv('.env')

def create_profile(context, username):
    while True:
        try:
            search = instaloader.TopSearchResults(context, username).get_profiles()
            profile = next(search)
            return profile
        except:
            username = random.choice(CELEBRITY_LIST)
            continue

def get_celebrity(only_one=False):
    if only_one:
        celebrity = random.choice(CELEBRITY_LIST)
        return create_profile(INSTALOADER.context, celebrity), None
    
    celebrity_one = random.choice(CELEBRITY_LIST)
    celebrity_two = random.choice(CELEBRITY_LIST)
    while celebrity_one == celebrity_two:
        celebrity_two = random.choice(CELEBRITY_LIST)
    
    celebrity_one = create_profile(INSTALOADER.context, celebrity_one)
    celebrity_two = create_profile(INSTALOADER.context, celebrity_two)
    return celebrity_one, celebrity_two
    
def compare_followers(choice, celebrity_one, celebrity_two):
    is_not_correct = True
    while is_not_correct:
        if choice == "A":
            if celebrity_one.followers > celebrity_two.followers:
                print("Correct!")
                is_not_correct = False
                return True, celebrity_one
            else:
                print("Wrong!")
                is_not_correct = False
                return False, False
        elif choice == "B":
            if celebrity_two.followers > celebrity_one.followers:
                print("Correct!")
                is_not_correct = False
                return True, celebrity_two
            else:
                print("Wrong!")
                is_not_correct = False
                return False, False
        else:
            print("Invalid input. Please type 'A' or 'B'")
            choice = input().upper()
    
def start_round(better):
    if better:
        print("have previous result")
        celebrity_one = better
        celebrity_two = get_celebrity(only_one=True)
    else:
        print("no previous result")
        celebrity_one, celebrity_two = get_celebrity()
        
    print(f"We are comparing {celebrity_one.username} and {celebrity_two.username}")
    print(f"For you who has more followers? Type 'A' for {celebrity_one.username} or 'B' for {celebrity_two.username}")
    user_choice = input().upper()
    result, better = compare_followers(user_choice, celebrity_one, celebrity_two)
    if not better:
        return  None
    else:
        return  better
    

if __name__ == "__main__":
    print(f"Welcome to the celebrity follower comparison game!")

    INSTALOADER = instaloader.Instaloader()
    INSTALOADER.login(os.getenv("INSTAGRAM_USERNAME"),os.getenv("INSTAGRAM_PASSWORD"))
    PREVIOUS_PROFILE = None
    
    winner = True
    better = None
    score = 0
    
    while True:
        print(better)
        better = start_round(better)
        if not better:
            winner = False
            break
        score += 1
        print(f"Your score is {score}")
        print("Do you want to play again? Type 'yes' or 'no'")
        play_again = input().lower()
        if play_again != "yes":
            break
              
    if not winner:
        print("Game over!")
    else:
        print("Congratulations! You won!")
        print(f"Your final score is {score}")
    
    