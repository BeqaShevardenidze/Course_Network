import main
import os
def Cls():
    os.system("cls")

def f_funk():
    print("""
    _________________Func_________________
    {1} - first func  
    {2} - fizzbuzz funck
    {3} - fizzbuzz funck argument
    {4} - Home Work V1
    {5} - Home Work V2
    {6} - Home Work ჩამოხრჩობანა
    {7} - Home Work ჩამოხრჩობანა Video
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
        case 5:
            name = input("what is your name?")
            def greeting(name):
                print(f"Hello {name}")
            greeting()
        case 6:
            import os
            import random
            Cls()
            arr = ['text', 'name', 'head', 'apple', 'banana']
            print("hello This is game:")
            def main():
                i = random.randint(0, 4)
                temp_word = arr[i]
                word = []
                old = []
                for i in temp_word:
                    word += i
                word2 = []
                for j in range(len(word)):
                    word2 += '_'
                
                while word != word2:
                    print(f"random word = {word}")
                    print(f"your word = {word2}")
                    num = -1
                    x = input("Chaweret erti aso >>>> ")
                    if x in word:
                        for j in word:
                            num += 1
                            if j == x:
                                word2[num] = x
                        Cls()
                        print(f"tqveni chawerili asoebi: {old}")
                        print('aseti aso aris')
                        if word == word2:
                            Cls()
                            print("Tqven moiget!!!")
                    else:
                        Cls()
                        old.append(x)
                        print(f"tqveni chawerili asoebi: {old}")
                        print('aseti aso ar aris')
            main()
        case 7:
            Cls()
            import random
            
            print("welcome to Hangman!")
            
            words = ["hacker", "bounty", "random"]
            secret_word = random.choice(words)
            print(secret_word)
            print("You get 5 Guesses")
            display_word = []
            for letter in secret_word:
                display_word += "_"
            print(display_word)

            num = 0
            game_over = False

            while not game_over:
                guess = input("Guess a letter ").lower()
                for position in range(len(secret_word)):
                    letter = secret_word[position]
                    if letter == guess:
                        display_word[position] = letter
                if guess not in secret_word:
                    num += 1
                    guesses_left = 5 - num
                    print(f"U have {guesses_left} life")
                    if num >= 5:
                        print("U Loser")
                        game_over = True
                print(display_word)

                if "_" not in display_word:
                    print("U Win")
                    game_over = True
        case _:
            print("ERROR")

if __name__ == "__main__":
    f_funk()