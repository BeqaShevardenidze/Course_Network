import main
def f_if_else_For_loop():
    main.Cls()
    print("""
    _________________If Else & For LOOP_________________
    {1} - If Else
    {2} - Home Work V1
    {3} - For Loop
    {4} - Home Work _ For loop V1
    {5} - 
""")
    
    x = int(input(">>>> "))
    match(x):
        case 1:
            print("_________If Else_________")
            fnum = input("What is the first number ")
            snum = input("What is the second number")
            if fnum > snum:
                print("The first number is bigger")
            elif fnum < snum:
                print("The second number is bigger")
            else:
                print("The numbers are same")
        case 2:
            print("_________Home Work V1_________")
            score = int(input("Enter your score: "))
            if score >= 90 and score <= 100:
                print("Scores 90 and above: Grade 'A'")
            elif score >= 80 and score <= 89:
                print("Scores 80 to 89: Grade 'B'")
            elif score >= 70 and score <= 79:
                print("Scores 70 to 79: Grade 'C'")
            elif score >= 60 and score <= 69:
                print("Score 60 to 69: Grade 'D'")
            elif score < 60:
                print("Score below 60: Grade 'F'")
        case 3:
            print("_________For Loop_________")
            fruits = ["apple", "banana", "cherry"]
            for fruit in fruits:
                print(fruit)
        case 4:
            for i in range(100):
                if i % 3 == 0 and i % 5 == 0:
                    print(f"{i} Fizzbuzz")
                elif i % 3 == 0:
                    print(f"{i} Fizz")
                elif i % 5 == 0:
                    print(f"{i} Buzz")
                else:
                    print(i)
        case 5:
            pass
        case _:
            print("ERROR")

if __name__ == "__main__":
    f_if_else_For_loop()