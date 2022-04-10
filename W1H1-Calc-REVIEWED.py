# variables should start with a lower case letter
# not necessary, as you could simply have "while True:"
Continue = "y"
while Continue == "y":

    # since you are not using variables, the 'f' is not needed at the beginning of your string
    # could use a multi-line string to avoid going too long in your line
    # could also create a variable outside of the while loop and use in place of this
    print(f"Welcome to the basic calculator!\nPlease make your selection: \n   1 for Addition \n   2 for Subtraction \n   3 for Multiplication \n   4 for Division")

    # not necessary - see https://docs.python.org/3.10/library/functions.html#input
    # could merge with part of the line above
    # is this variable mnemonic (memorable)? Would you know what it was for if you came back months later?
    NewVar = input()

    if not NewVar:
        # what is the user experience here?
        #   - They have to start it over again - extra steps
        #   - never indicated that empty input would exit the program
        print("No Value Entered. Thanks for using the calculator! Goodbye!")

        # instead of break, you could simply use continue and it would start over
        break

    # nice use of the built-in for str to test if it's numeric!
    # another option is to see if the string is in a list or tuple of strings you expect
    # or you could test if numeric and then if in a list/tuple of integers
    # - might be problematic if they do a float & not type cast to int
    elif not str.isnumeric(NewVar):
        # what is the user experience here? They have to start it over again - extra steps
        print("Non Numeric Value Entered. Please run again and select a number, 1-4.")

        # how is the user experience with this? Did you inform them it would end if nothing was provided?
        # instead of break, you could simply use continue and it would start over
        print("Thanks for using the calculator! Goodbye!")
        break

    # why did you type case the string to float and then int? Why not just int?
    NewVar = int(float(NewVar))

    # I see this was made for incorrect attempts - how is the user experience?
    Count = 0

    if NewVar >= 1 and NewVar <= 4:
        Test = 1
    else:
        # instead of this, you could simply use the print statements in the next internal while loop
        # and then continue to start back up at the top of the first while loop
        Test = 2

    # why do another loop when you already have the external loop that could catch this?
    while Test > 1:
        # this could have been handled earlier when they enter nothing or non-numeric
        print("Invalid selection!")

        # this is duplicate lines since you have it at the beginning
        # this internal loop is causing you to have unnecessary code
        print(f"Please make your selection: \n   1 for Addition \n   2 for Subtraction \n   3 for Multiplication \n   4 for Division")

        # what is the user experience like?
        # this changes how your code looks to the user (changes their expectations)
        print("Or hit enter to exit.")

        # unnecessary since you are immediately assigning it to the returned data from input
        NewVar2 = None
        NewVar2 = input()

        if not NewVar2:
            # this will cause the code to completely end, meaning ...
            # after they choose an option, if they don't provide input they have to start over
            print("No Value Entered. Thanks for using the calculator! Goodbye!")

            # this ends both the outer while
            Continue = "n"
            # this breaks the inner while
            break

        elif not str.isnumeric(NewVar2):
            # what is the user experience here?
            print("Non Numeric Value Entered. Please run again and select a number, 1-4.")
            # is this really goodbye?
            print("Thanks for using the calculator! Goodbye!")
            # this only breaks/ends the inner loop but it will start at the very beginning of your code from here
            # and also resets your counter, since it's only used in the inner loop & is created in the outer loop
            break

        # why create a new variable? Why not use the one you originally made?
        NewVar2 = int(float(NewVar2))
        if NewVar2 >= 1 and NewVar2 <= 4:
            # ends inner While loop
            Test = 1
            # you are assigning this NewVar2 into NewVar
            NewVar = NewVar2

        elif Count == 5:
            print("Too many incorrect selections made.")
            print("Thank you for using the calculator! Goodbye!")
            # this only break the internal loop - starts back at the top of external While loop
            break

        # this section of code will never be hit
        else:
            print("Else Statment")
            Test = 2
            Count = Count+1

    # for this if-else section, you reuse a lot of the same code ...
    # how might you be able to clean this up, minimize code, and enhance the user experience?
    if NewVar == 1:
        print("You have selected Addition")

        # next 2 lines could be 1 line
        print("Enter your first number:", end=" ")
        FirstNumber = input()

        # you didn't check to ensure that the input would be a number
        FirstNumber = float(FirstNumber)

        # these could be all 1 line
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = float(SecondNumber)

        Solution = FirstNumber+SecondNumber

        # could use f-string formatting
        # all of this chunk of lines could be 1-2 lines
        print(FirstNumber, " + ", SecondNumber, " = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()

        # what is the user experience if they do "Y" or "y "?
        # consider using built in str methods like:
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.lower
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.upper
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.strip
        if Continue == "y":
            Continue = "y"
        else:
            # what is the user experience? what if they mis-typed or wanted to go again?
            print("Thank you for using the Calculator! Goodbye")

    elif NewVar == 2:
        # these could be on the same line
        print("You have selected Subtraction")
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = float(FirstNumber)

        # these could be on the same line & no testing if a number
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = float(SecondNumber)

        Solution = FirstNumber-SecondNumber

        # these could be on the same line
        print(FirstNumber, " - ", SecondNumber, " = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()

        # what is the user experience if they do "Y" or "y "?
        # consider using built in str methods like:
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.lower
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.upper
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.strip
        if Continue == "y":
            Continue = "y"
        else:
            # what is the user experience? what if they mis-typed or wanted to go again?
            print("Thank you for using the Calculator! Goodbye")

    elif NewVar == 3:
        print("You have selected Multiplication")

        # these could be on the same line & no testing if a number
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = float(FirstNumber)

        # these could be on the same line
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = float(SecondNumber)

        Solution = FirstNumber*SecondNumber

        # these could be on the same line
        print(FirstNumber, " x ", SecondNumber, " = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()

        # what is the user experience if they do "Y" or "y "?
        # consider using built in str methods like:
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.lower
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.upper
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.strip
        if Continue == "y":
            Continue = "y"
        else:
            # what is the user experience? what if they mis-typed or wanted to go again?
            print("Thank you for using the Calculator! Goodbye")

    elif NewVar == 4:
        print("You have selected Division")

        # these could be on the same line & no testing if a number
        print("Enter your first number:", end=" ")
        FirstNumber = input()
        FirstNumber = int(float(FirstNumber))

        # these could be on the same line & no testing if a number
        print("Enter your second number:", end=" ")
        SecondNumber = input()
        SecondNumber = int(float(SecondNumber))

        Solution = FirstNumber/SecondNumber

        # these could be on the same line
        print(FirstNumber, " / ", SecondNumber, " = ", Solution)
        print(" ")
        print("Would you like to use the calculator again? (y/n)  ", end=" ")
        Continue = input()

        # what is the user experience if they do "Y" or "y "?
        # consider using built in str methods like:
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.lower
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.upper
        #   https://docs.python.org/3.10/library/stdtypes.html?highlight=str#str.strip
        if Continue == "y":
            Continue = "y"
            print(f"\n \n")

        else:
            # what is the user experience? what if they mis-typed or wanted to go again?
            print("Thank you for using the Calculator! Goodbye")
    print(f"\n")
