import random
# num = random.random()
# print(num)


# #Python pogram for fenerationg a random integer
# num1 = random.randint(1,500)
# print(num1)

# #To generate value between a specific range
# num2 = random.randrange(1,10)
# print(num2)

# num3 = random.randrange(1,10,2)
# print(num3)


# #To select a random element
# random_s = random.choice("Random Module")#a string
# print(random_s)
# random_l = random.choice([12,54,765,23,45,45])#a list
# print(random_l)
# random_k = random.choice((12,64,23,54,34))
# print(random_k)

# list1 = [34,23,65,86,23,43]
# random.shuffle(list1)
# print(list1)
# random.shuffle(list1)
# print(list1)


def start_game():
    # Function to play game  
    print("This is javatpoint's Rock-Paper-Scissors!")
    print("Please Enter your choice:")
    print("Choice 1: Rock")
    print("Choice 2: Paper")
    print("Choice 3: Scissors")

#To take the user input      
    choice_user = int(input("Select any options from 1-3"))

    # randint() Function which generates a random number by computer  
    choice_machine = random.randint(1, 3)  

    # display the machines choice  
    print("Option choosed by Machine is :",end="")
    if choice_machine == 1:
        print("Rock")
    elif choice_machine == 2:
        print("Paper")
    elif choice_machine == 3:
        print("Scissors")

    # To declare who the winner is  
    if choice_user == 1 and choice_machine == 3: 
        print(" Congratulations!! You won! ")
    elif choice_user == 2 and choice_machine == 1:
        print(" Congratulations!! You won! ") 
    elif choice_user == 3 and choice_machine == 2:  
        print(" Congratulations!! You won! ")
    else:  
        print(" Sorry! The Machine Won the Game? ") 
    

    # If user wants to play again  

    play_again = input(" Want to Play again? ( yes / no ) ").lower()  
    if play_again == "yes":  
        start_game()  
    else:  
        print(" Thanks for playing Rock-Paper-Scissors! ")  
 


start_game()