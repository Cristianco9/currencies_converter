#!/user/bin/env python

import sys
how_much = 0
you_have = 0
usd = 4435
mxn = 221
eur = 4438
arg = 31

def cop_to_usd():
    print("\n********************** COP TO USD ***********************")
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / usd
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Dollars")
    print("************************* DONE **************************")

def cop_to_mxn():
    print("\n********************** COP TO MXN ***********************")
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / mxn
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Mexican Pesos")
    print("************************* DONE **************************")

def cop_to_eur():
    print("\n********************** COP TO EUR ***********************")
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / eur
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Euros")
    print("************************* DONE **************************")

def cop_to_arg():
    print("\n********************** COP TO USD ***********************")
    how_much= float(input("Please enter the amount of pesos to convert: "))
    you_have = how_much / arg
    you_have = round(you_have, 2)
    you_have = str(you_have)
    print("You have $" + you_have + " Argentine Pesos")
    print("************************* DONE **************************")

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

    choose = int(input("Please enter a number from (1-5): "))
    while choose < 1 or choose > 5:
        print("********************** WRONG VALUE **********************")
        choose = int(input("\nPlease enter a number from (1-5): "))
        print("*********************************************************")
   
    print("*********************************************************")

    if choose == 1:
        cop_to_usd()

    elif choose == 2:
        cop_to_mxn()

    elif choose == 3:
        cop_to_eur()

    elif choose == 4:
        cop_to_arg()

    elif choose == 5:
        sys.exit("********************* PROGRAM ENDED *********************")

    else:
        print("********************** WRONG VALUE **********************")
        sys.exit("********************* PROGRAM ENDED *********************")
