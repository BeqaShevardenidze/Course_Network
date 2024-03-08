import main

def f_funk():
    print("""
    _________________Func_________________
    {1} - first func  
    {2} - fizzbuzz funck
    {3} - fizzbuzz funck argument
    {4} - Home Work
    """)
    x = int(input(">>>> "))
    match x:
        case 1:
            def function():
                print("hello")
            function()
        case 2:
            def function():
                for i in range(100):
                    if i % 3 == 0 and i % 5 == 0:
                        print(f"{i} Fizzbuzz")
                    elif i % 3 == 0:
                        print(f"{i} Fizz")
                    elif i % 5 == 0:
                        print(f"{i} Buzz")
                    else:
                        print(i)
            function()
        case 3:
            choise = int(input("what number u want to choise? "))
            def function(choise):
                for i in range(choise):
                    if i % 3 == 0 and i % 5 == 0:
                        print(f"{i} Fizzbuzz")
                    elif i % 3 == 0:
                        print(f"{i} Fizz")
                    elif i % 5 == 0:
                        print(f"{i} Buzz")
                    else:
                        print(i)
            function(choise)
        case 4:
            name = input("what is your name? >>>>")
            def function():
                print(f"Hello {name}")
            function()
            # 1:11 
        case _:
            print("ERROR")

if __name__ == "__main__":
    f_funk()