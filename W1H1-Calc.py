Continue="y"
while Continue=="y":
    print(f"Welcome to the basic calculator!\nPlease make your selection: \n   1 for Addition \n   2 for Subtraction \n   3 for Multiplication \n   4 for Division")
    NewVar=input()
    if not NewVar:
        print("No Value Entered. Thanks for using the calculator! Goodbye!")
        break
    elif not str.isnumeric(NewVar):
        print("Non Numeric Value Entered. Please run again and select a number, 1-4.")
        print("Thanks for using the calculator! Goodbye!")
        break
    NewVar=int(float(NewVar))
    Count=0
    if NewVar>=1 and NewVar<=4:
        Test=1
    else:
        Test=2
    while Test>1:
        print("Invalid selection!")
        print(f"Please make your selection: \n   1 for Addition \n   2 for Subtraction \n   3 for Multiplication \n   4 for Division")
        print("Or hit enter to exit.")
        NewVar2=None
        NewVar2=input()
        if not NewVar2:
            print("No Value Entered. Thanks for using the calculator! Goodbye!")
            Continue="n"
            break
        elif not str.isnumeric(NewVar2):
            print("Non Numeric Value Entered. Please run again and select a number, 1-4.")
            print("Thanks for using the calculator! Goodbye!")
            break
        NewVar2=int(float(NewVar2))
        if NewVar2 >= 1 and NewVar2 <= 4:
            Test=1
            NewVar=NewVar2
        elif Count==5:
            print("Too many incorrect selections made.")
            print("Thank you for using the calculator! Goodbye!")
            break
        else:
            print("Else Statment")
            Test = 2
            Count = Count+1
    if NewVar==1:
        print("You have selected Addition")
        print("Enter your first number:", end=" ")
        FirstNumber=input()
        FirstNumber=float(FirstNumber)
        print("Enter your second number:", end=" ")
        SecondNumber=input()
        SecondNumber=float(SecondNumber)
        Solution=FirstNumber+SecondNumber
        print(FirstNumber," + ", SecondNumber," = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue=input()
        if Continue=="y":
            Continue="y"
        else:
            print("Thank you for using the Calculator! Goodbye")

    elif NewVar==2:
        print("You have selected Subtraction")
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = float(FirstNumber)
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = float(SecondNumber)
        Solution=FirstNumber-SecondNumber
        print(FirstNumber," - ", SecondNumber," = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()
        if Continue == "y":
            Continue = "y"
        else:
            print("Thank you for using the Calculator! Goodbye")
    elif NewVar==3:
        print("You have selected Multiplication")
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = float(FirstNumber)
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = float(SecondNumber)
        Solution=FirstNumber*SecondNumber
        print(FirstNumber," x ", SecondNumber," = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()
        if Continue == "y":
            Continue = "y"
        else:
            print("Thank you for using the Calculator! Goodbye")
    elif NewVar==4:
        print("You have selected Division")
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = int(float(FirstNumber))
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = int(float(SecondNumber))
        Solution=FirstNumber/SecondNumber
        print(FirstNumber," / ", SecondNumber," = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()
        if Continue == "y":
            Continue = "y"
            print(f"\n \n")

        else:
            print("Thank you for using the Calculator! Goodbye")
    print(f"\n")
