# driver code

import os
from sys import exit
from currConv import Converter

converter = Converter.Converter()

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


while True:

    screen_clear()
    print('\n          - REAL TIME CURRENCY CONVERTER - \n')

    print('\n1. Open Converter\n2. View Supported Country Codes\n3. EXIT\n')
    try:
        choice = int(input('\n-> Enter your choice : '))
    
        if choice == 1:
            screen_clear()
            print('\n       - CURRENCY CONVERTER - \n')
            fromCur = input("-> Enter source Currency Code : ").upper()
            toCur = input("-> Enter target Currency Code : ").upper()

            # for name in converter.rates:
            #     if (fromCur or toCur ) != converter.rates[name]:
            #         print("\n-> Please enter valid currency code.")
            #         break
                
            amt = float(input("\n-> Enter amount : "))

            converter.convert(amt, fromCur, toCur)
            # use this if you return values from converter.convert()
            # print(f'\n\n{converter.convert(amt, fromCur, toCur)}')

        elif choice == 2:
            screen_clear()
            print('\n       - Supported Country Codes - \n')
            i = 0
            for name in converter.rates:
                if converter.rates[name]:
                    i+=1
                    print(f'{i}. {name}')

        elif choice == 3:
            exit()

        else:
            print('\n\n -- Please select a valid option.')    

    except ValueError:
        print('\n\n -- Please enter valid values.')

    except KeyError:
        print('\n\n -- Please enter valid currency code')

    input("\n// Press ENTER to continue")

