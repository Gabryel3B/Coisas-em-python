import os
import shutil

cardapio = []
contador = 0

print("Criador de lista")
c = input("O que terá na sua lista: ")
b = int(input("Insira quantos itens terá na sua lista: "))

while True:
    a = input("Diga o item "+str(contador+1)+": ")
    cardapio.append(a)
    contador+=1
    if contador >= b:
        break

print("\nSua lista foi:\n\nLista de "+c)
for i in cardapio:
    print("- "+i)

text = input("Vc gostaria de criar um arquivo txt com sua lista? (S/N): ")

if text == "S":
    if not os.path.exists("Listas"):
        os.mkdir("Listas")

    with open(c+".txt", "w") as file:
        file.write(str(cardapio))

    shutil.move(c+".txt","Listas")

    print("Tudo feito! Obrigado!")

else:
    print("Ok, até a próxima!")