
print ("                                              Welcome to the Rock, Paper, Scissors Game!")
print ("  ---Write the answers you want to give against the questions asked to you. Your answers other than rock, paper, scissors are not accepted.---")
print ("                             The winner of the round gets 1 point. In the event of a tie, no points are awarded.")
print ("                      ---The side that wins 2 rounds in the game will be considered the winner of the game. Good luck!---")

username = input("What is your username? ")

print( username, end="!\n")

import random

def rock_paper_scissors_choice_of_computer():
    n = random.randint(1,3)
    if n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"
        

user_score = 0
computer_score = 0

while True:
    user_choice = input("Serkan Susur____"  "   rock? paper? scissors?:  ")

    if user_choice not in ["rock", "paper", "scissors"]:
        print("lnvalid selection, please type 'rock', 'paper' or 'scissors'.")
        continue

    computer_choice = rock_paper_scissors_choice_of_computer()
    print("Computer:", computer_choice)
     
    if computer_choice == user_choice:
        user_score == 0 and computer_score == 0
    elif computer_choice == "rock" and user_choice == "paper":
        user_score += 1
    elif computer_choice == "paper" and user_choice == "scissors":
        user_score += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        user_score += 1
    else:
        computer_score += 1
    print("You:", user_score, "VS Computer:", computer_score )

    if user_score == 2 or computer_score == 2:
        break


if computer_score > user_score:
    print("YOU LOST :( ")
else:
    print("YOU WON :) CONGRATULATIONS", username)


import random

def computer_answer():
    return random.choice(["yes", "no"])

def play_again():
    user_reply = input("Would you like to play again? (yes/no): ").strip().lower()
    if user_reply not in ["yes", "no"]:
        print("lnvalid selection, please type 'rock', 'paper' or 'scissors'.")
        return play_again()
    return user_reply

while True:

    user_reply = play_again()
    
    cmpt_reply = computer_answer()
    print("Computer's answer:", cmpt_reply)

    if user_reply == "yes" and cmpt_reply == "yes":
        print("The computer has accepted your challenge!")
    elif user_reply == "yes" and cmpt_reply == "no":
        print("The computer was scared of you and ran away!")
        break
    elif user_reply == "no" and cmpt_reply == "yes":
        print("The computer is laughing at you! :)) ")
        break
    elif user_reply == "no" and cmpt_reply == "no":
        print("The producer of the game thinks you are both incompetent :)")
        break
    
    

    import random

    def rock_paper_scissors_choice_of_computer():
        n = random.randint(1,3)
        if n == 1:
            return "rock"
        elif n == 2:
            return "paper"
        else:
            return "scissors"
        

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("rock? paper? scissors?:  ")

        if user_choice not in ["rock", "paper", "scissors"]:
            print("lnvalid selection, please type 'rock', 'paper' or 'scissors'.")
            continue

    
        computer_choice = rock_paper_scissors_choice_of_computer()
        print("Computer:", computer_choice)
     
        if computer_choice == user_choice:
            user_score == 0 and computer_score == 0
        elif computer_choice == "rock" and user_choice == "paper":
            user_score += 1
        elif computer_choice == "paper" and user_choice == "scissors":
            user_score += 1
        elif computer_choice == "scissors" and user_choice == "rock":
            user_score += 1
        else:
            computer_score += 1
            print("You:", user_score, "VS Computer:", computer_score )

        if user_score == 2 or computer_score == 2:
            break


    if computer_score > user_score:
        print("YOU LOST :( ")
    else:
        print("YOU WON :) CONGRATULATIONS", username)


    

print("Game over. Press enter to exit...")
input()


  



