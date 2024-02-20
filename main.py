import os
from importlib import reload

import print_variables
def Cls():
    os.system("cls")
Cls()

while True:
    print("""
    _________________Main Menu_________________
    {1} - Print & Variables
    """)

    x = int(input(">>>> "))

    match x:
        case 1:
            Cls()
            reload(print_variables)
            from print_variables import f_1_print_variables
            f_1_print_variables()
        case _:
            Cls()
            print("ERROR")