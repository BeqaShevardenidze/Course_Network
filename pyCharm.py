def f_pyCharm():
    print("""
    _________________PyCharm_________________
    {1} - PyCharm Install
    """)
    x = int(input(">>>> "))
    match x:
        case 1:
            pass
        # 1:34
        case _:
            print("ERROR")

if __name__ == "__main__":
    f_pyCharm()