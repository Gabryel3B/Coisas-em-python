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

