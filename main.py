import os
from importlib import reload

import print_variables
import if_else_For_loop
import funk
def Cls():
    os.system("cls")
Cls()

while True:
    print("""
    _________________Main Menu_________________
    {1} - Print & Variables
    {2} - If Else & For Loop
    {3} - Func
    """)

    x = int(input(">>>> "))

    match x:
        case 1:
            Cls()
            reload(print_variables)
            from print_variables import f_1_print_variables
            f_1_print_variables()
        case 2:
            Cls()
            reload(if_else_For_loop)
            from if_else_For_loop import f_if_else_For_loop
            f_if_else_For_loop()
        case 3:
            Cls()
            reload(funk)
            from funk import f_funk
            f_funk()
        case _:
            Cls()
            print("ERROR")