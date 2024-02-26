import main

def f_funk():
    print("""
    _________________Func_________________
    {1} - first func  
    {2} - fizzbuzz   
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
        case _:
            print("ERROR")

        # 1:04


if __name__ == "__main__":
    f_funk()