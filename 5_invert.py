x = int(input(""))
inv = int(str(x)[::-1])


if 1000 <= x <= 9999:
    print(inv)
else : print("Insira um número entre 1000 e 9999.")
