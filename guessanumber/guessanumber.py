import random

# display the game rules
print("Lets play guess a number In this game you have to guess corret number between 1 to 100 You have to guess number in less attempt")
# generating random number 
computerguess=random.randint(1,100)
# variable for counting the gameloop
i=0
# gameloop
while(i<=1):
    while(True):
        i=i+1
        # taking input from user
        userguess=int(input("Enter your guess number:\n"))

        # game conditions
        if(userguess==computerguess):
            print(f"Your guess is right \nYou guess number in {i} Times")
            break
        elif(userguess<=computerguess):
            print("your guess is low")
        elif(userguess>=computerguess):
            print("your guess is high")
        else:
            print("Please enter valid guess")
    print("Thanks for playing")
    
    


