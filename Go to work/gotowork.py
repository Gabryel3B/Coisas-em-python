import random
import os

start = None

os.system('cls')
print("Bem vindo!\nAgora siga pro teu trabalho mlk")
conf = input("Pronto pra sair? (S/N): ").upper()

if conf == "S":
    start = True

else:
    print("Ok então né")

while start == True:
    field = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",
             "_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",
             "_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",
             "_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]

    building = ["D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D",
             "D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D",
             "D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D",
             "D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D"]

    player = ["i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i",
             "i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i",
             "i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i",
             "i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i"]

    buil = random.randrange(len(field))
    ya = random.randrange(len(field))

    if buil == ya:
        buil = 22

    count = 0

    while buil != ya:
        os.system('cls')
        field[buil] = building[buil]
        field[ya] = player[ya]
        if count > 0:
            print("Movimentos usados: " + str(count))

        print("".join(field[:18]))
        print("".join(field[18:36]))
        print("".join(field[36:54]))
        print("".join(field[54:]))

        dir = input("Pra onde você vai? (d/c/b/e): ")

        if dir == "e":
            field[ya] = "_"
            ya = ya -1
            count += 1

        elif dir == "d":
            field[ya] = "_"
            ya = ya +1
            count += 1

        elif dir == "c":
            field[ya] = "_"
            ya = ya -18
            count += 1

        elif dir == "b":
            field[ya] = "_"
            ya = ya +18
            count += 1

    os.system('cls')
    print("Você chegou ao trabalho!")

    final = input("Quer jogar novamente? (S/N): ").upper()

    if final == "S":
        continue

    else:
        print("Até a próxima!")
        break