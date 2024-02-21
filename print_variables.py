from main import Cls
def f_1_print_variables():
    print("""
    _________________Print & variables_________________
    {1} - Print
    {2} - string var
    {3} - input V1
    {4} - input V2
    {5} - Var Int
    {6} - Home Work 1
    {7} - Home Work 2
    """)
    x = int(input(">>>> "))
    match x:
        case 1:
            print("hello world 1")
            print("hello world 2")
            print("hello world 3")
            print("-------------\n")
            print("hello world 1 \nhello world 2")
            print("-------------\n")
            print("Ryan" + " John")
            print("Ryan" + " " + "John")
        case 2:
            print("\n------Var-------")
            x = 'Ryan'
            y = 'john'
            print(f"{x} {y}")
        case 3:
            print("\n------input V1-------")
            ip = input('What is the target ip? ')
            print("The ip u entered is ",ip)
        case 4:
            print("\n------input V2-------")
            print("The ip u entered is " + input('What is the target ip? '))
        case 5:
            print("\n------Var Int-------")
            x = 5
            y = 'John'
            print(str(x) + " " + y)
        case 6:
            print("\n------Home Work 1-------")
            x = input('What is your name? ')
            y = input('What is your last name? ')
            print(f"U are: {x} {y}")
            # Stoped Time 27:33 
        case 7:
            print("\n------Home Work 2-------")
            print("Thanks for using my program!")
            pet_name = input("Enter your pet name! ")
            born_sity = input("Where u Born? ")
            nick_name = "@cyber" + pet_name
            print(f"Your new handle and bio {nick_name} from {born_sity}")
            # 35:16




if __name__ == "__main__":
    Cls()
    f_1_print_variables()