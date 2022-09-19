# Program to converter Colombian Pesos to several currencies

# Shebang | interpreter path
#!/user/bin/env python

# Importing a system module to can exit the program with the option number 5
import sys

# Variable to save the user amount
how_much = 0
# variable to save the converted user amount
you_have = 0

# Variables to save the currencies equivalent in Colombian Pesos 
usd = 4435
mxn = 221
eur = 4438
arg = 31

# functions
def cop_to_usd():
    """Function to calcule the convertion and print the result"""
    print("\n********************** COP TO USD ***********************")
    # Amount request
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / usd
    # Limit the amount to only 2 decimal places
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Dollars")
    print("************************* DONE **************************")

def cop_to_mxn():
    """Function to calcule the convertion and print the result"""
    print("\n********************** COP TO MXN ***********************")
    # Amount request
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / mxn
    # Limit the amount to only 2 decimal places
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Mexican Pesos")
    print("************************* DONE **************************")

def cop_to_eur():
    """Function to calcule the convertion and print the result"""
    print("\n********************** COP TO EUR ***********************")
    # Amount request
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / eur
    # Limit the amount to only 2 decimal places
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Euros")
    print("************************* DONE **************************")

def cop_to_arg():
    """Function to calcule the convertion and print the result"""
    print("\n********************** COP TO USD ***********************")
    # Amount request
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / arg
    # Limit the amount to only 2 decimal places
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Argentine Pesos")
    print("************************* DONE **************************")

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
        cop_to_usd()

    elif choose == 2:
        cop_to_mxn()

    elif choose == 3:
        cop_to_eur()

    elif choose == 4:
        cop_to_arg()
    # option to close the program
    elif choose == 5:
        sys.exit("********************* PROGRAM ENDED *********************")
    # If the user enter a wrong input close the program 
    else:
        print("********************** WRONG VALUE **********************")
        sys.exit("********************* PROGRAM ENDED *********************")
