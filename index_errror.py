import random
user_choice=int(input("Enter your choice:Type 0 for rock,1 for papers and 2 for scissors:"))
computer_choice=random.randint(0,2)
print("computer_choice:")
print(computer_choice)
if computer_choice==0 and user_choice==2:
    print("you lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice > user_choice:
    print("you lose")
elif computer_choice<user_choice:
    print("you win")
elif computer_choice==0 and user_choice==0:
    print("it's draw")