# this game is a rock paper scissor game between a user and a computer
import random
choice = ["Rock", "Paper", "Scissor"]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor: \n"))
computer_choice = random.randint(0, 2)
print(f"computer chose: {computer_choice}\n")
# check on the condition of choices based on the rules of the game

if your_choice >=3 or your_choice <0: 
    print("You typed an invalid number, you lose!")
elif your_choice ==0 and computer_choice ==2:
    print("You win!")
elif computer_choice == 0 and your_choice ==2:
    print("You lose!")
elif computer_choice > your_choice :
    print("You lose!")
elif your_choice > computer_choice :
    print("You win!")
elif computer_choice == your_choice : 
    print("It's a draw!")
    
