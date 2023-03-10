password = input("Enter password: ")
while password != "0812": 
    password = input("Wrong password. Try again: ")

if(password == "0812"):
    print("Welcome to Calculator!")



def Calculator():
    print("1) Add\t2)Subtract\n3)Multiply\t4)Divide")
    a = int(input("Type 1/2/3/4 according to the operation you would like to try: "))
    if(a == 1):
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("The sum is ", a1+a2)
        #a = int(input("Which one would you like to try this time (1/2/3/4?): "))
    elif(a == 2):
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("The difference is ", a1-a2)
        #a = int(input("Which one would you like to try this time (1/2/3/4?): "))

    elif(a == 3):
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("The product is ", a1*a2)
        #a = int(input("Which one would you like to try this time (1/2/3/4?): "))

    elif(a == 4):
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("The quotient is ", a1/a2)
        #a = int(input("Which one would you like to try this time (1/2/3/4?): "))
    repeat = input("Would you like to run again? y/n ")
    if (repeat == "y"):
        Calculator() 
    elif (repeat == "n"):
        print("Thank you")    

Calculator()
   
