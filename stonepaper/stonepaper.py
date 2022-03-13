import random
print("Lets play stone paper scissor \n 1 for stone \n 2 for paper \n 3 for scissor")

# variables
i=0
computerpoint=0
userpoint=0

# gameloop
while(i<=5):
    # taling input
    userplay=int(input("Enter your play:")) # taking user input
    computerplay=random.randint(1,3) #taking computer input

    # printing computer input
    print(f"computer play is: {computerplay}")

    # game condition
    if(userplay==computerplay):
        print("Both are winner")
    elif(userplay==1 and computerplay==3):
        print("You are winner") 
        userpoint = userpoint + 1  
    elif(userplay==2 and computerplay==1):
        print("You are winner")
        userpoint = userpoint + 1
    elif(userplay==3 and computerplay==2):
        print("You are winner")
        userpoint = userpoint + 1
    elif(userplay==1 and computerplay==2):
        print("You are loser")
        computerpoint = computerpoint + 1
    elif(userplay==2 and computerplay==3):
        print("You are loser")
        computerpoint = computerpoint + 1
    elif(userplay==3 and computerplay==1):
        print("You are loser")
        computerpoint = computerpoint + 1
    else:
        print("Please enter valid number")
    i=i+1

# printing points of user and computer
print(f"your points : {userpoint}") # printing userpoint  
print(f"computer points : {computerpoint}") # printing computer point

# calculating the points of user and computer ,and print the winner
if computerpoint == userpoint:
    print("Its a tie")
elif computerpoint > userpoint:
    print("computer wins")
elif computerpoint < userpoint:
    print("you wins")
