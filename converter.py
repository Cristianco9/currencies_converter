#!/user/bin/env python

import sys

while True:     
    print("*****************************************************")
    print("*************** CALCULATE CURRENCIES ****************")
    print("*****************************************************")
    print("* 1) Calculate COP to USD                           *")
    print("* 2) Calculate USD to MXN                           *")
    print("* 3) Calculate COP to MXN                           *")
    print("* 4) Calculate USD to ARG                           *")
    print("* 5) exit                                           *")
    print("*****************************************************")

    choose = int(input("\nPlease enter a number from (1-5): "))
    while choose < 1 or choose > 5:
        print("******************** WRONG VALUE ********************")
        choose = int(input("\nPlease enter a number from (1-5): "))
        print("*****************************************************")
   
    if choose == 1:
        print("good") 

    elif choose == 2:
        print("good") 

    elif choose == 3:
        print("good") 

    elif choose == 4:
        print("good") 

    elif choose == 5:
        print("good") 
        sys.exit("******************* PROGRAM ENDED *******************")

    else:
        print("******************** WRONG VALUE ********************")
        sys.exit("******************* PROGRAM ENDED *******************")
