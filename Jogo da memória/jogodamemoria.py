import os
import random
from time import sleep

while True:
    os.system('cls')
    linha1 = ["[!]","[?]","[.]","[;]"]
    linha2 = ["[!]","[?]","[.]","[;]"]
    card1 = ["[*]","[*]","[*]","[*]"]
    card2 = ["[*]","[*]","[*]","[*]"]

    random.shuffle(linha1)
    random.shuffle(linha2)

    while card1.count("[*]") > 0 and card2.count("[*]") > 0:
        print(" ".join(card1))
        print(" ".join(card2))
        l1 = int(input("Escolha a carta na linha 1: "))
        if card1[l1-1] != "[*]":
            print("Essa carta já foi revelada!")
            sleep(2)
            os.system('cls')
            continue
        card1[l1-1] = linha1[l1-1]
        os.system('cls')
        print(" ".join(card1))
        print(" ".join(card2))

        l2 = int(input("Escolha a carta na linha 2: "))
        if card2[l2-1] != "[*]":
            print("Essa carta já foi revelada!")
            sleep(2)
            os.system('cls')
            card1[l1 - 1] = "[*]"
            continue
        card2[l2-1] = linha2[l2-1]

        os.system('cls')
        print(" ".join(card1))
        print(" ".join(card2))

        if card1[l1-1] == card2[l2-1]:
            os.system('cls')
            continue

        else:
            sleep(3)
            os.system('cls')
            card1[l1 - 1] = "[*]"
            card2[l2 - 1] = "[*]"
            continue

    final = input("Quer jogar novamente? (S/N): ").upper()

    if final == "S":
        continue

    else:
        print("Até a próxima!")
        break