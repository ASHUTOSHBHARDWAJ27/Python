while(True):  
    # taking input from user
    number1=int(input("Enter the 1st number:\n")) 
    operation=input("Enter the operation:\n")
    number2=int(input("Enter the 2nd number:\n"))
    
    # calculating the numbers
    if(operation=='+'):
        print(f"The sum of two number is:{number1+number2}")
    elif(operation=='-'):
        print(f"The subtraction of two number is:{number1-number2}")
    elif(operation=='*'):
        print(f"The product of two number is:{number1*number2}")
    elif(operation=='/'):
        print(f"The divison of two number is:{number1/number2}")
    else:
        print("Invalid input")

 


 