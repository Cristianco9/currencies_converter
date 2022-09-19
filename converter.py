# Program to converter Colombian Pesos to several currencies

# Shebang | interpreter path
#!/user/bin/env python

# Importing a system module to can exit the program with the option number 5
import sys

# Variable to save the user amount
how_much = 0
# variable to save the converted user amount
you_have = 0

# function
def converter(currencie):
    """Function to calcule the convertion and print the result"""
    # Amount request
    print("Please enter the amount of Colombian Pesos to convert:")
    how_much= float(input(">>>"))
    you_have = how_much / currencie
    # Limit the amount to only 2 decimal places
    you_have = round(you_have, 2)
    you_have = str(you_have)
    return you_have

# Options menu
while True:     
    print("\n*********************************************************")
    print("***************** CALCULATE CURRENCIES ******************")
    print("*********************************************************")
    print("* 1) Calculate COP to USD                               *")
    print("* 2) Calculate COP to MXN                               *")
    print("* 3) Calculate COP to EUR                               *")
    print("* 4) Calculate COP to ARG                               *")
    print("* 5) exit                                               *")
    print("*********************************************************")

    # Loop to validate the user input
    choose = int(input("Please enter a number from (1-5): "))
    while choose < 1 or choose > 5:
        print("********************** WRONG VALUE **********************")
        choose = int(input("Please enter a number from (1-5): "))
   
    print("*********************************************************")

    # Assign a function to the validated option
    if choose == 1:
        print("\n********************** COP TO USD ***********************")
        final_amount = converter(4435)
        print("You have $" + final_amount + " Dollars")
        print("************************* DONE **************************")

    elif choose == 2:
        print("\n********************** COP TO MXN ***********************")
        final_amount = converter(221)
        print("You have $" + final_amount + " Mexican Pesos")
        print("************************* DONE **************************")

    elif choose == 3:
        print("\n********************** COP TO EUR ***********************")
        final_amount = converter(4438)
        print("You have $" + final_amount + " Euros")
        print("************************* DONE **************************")

    elif choose == 4:
        print("\n********************** COP TO ARG ***********************")
        final_amount = converter(31)
        print("You have $" + final_amount + " Argentine Pesos")
        print("************************* DONE **************************")

    # option to close the program
    elif choose == 5:
        sys.exit("********************* PROGRAM ENDED *********************")

    # If the user enter a wrong input close the program 
    else:
        print("********************** WRONG VALUE **********************")
        sys.exit("********************* PROGRAM ENDED *********************")
