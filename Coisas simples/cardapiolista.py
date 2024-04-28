comidas = ["Pizza","Pastel","Sorvete","Macarrão"]
bebidas = ["Coca","Pepsi","Guaraná","Fanta"]

print("CARDÁPIO\nEscolha o seu pedido\n1) Pizza\n2) Pastel\n3) Sorvete\n4) Macarrão")

a = int(input("\nDiga seu pedido: "))
b = input("Quer alguma bebida? (s/n): ")

if b == "s":
    print("CARDÁPIO\nEscolha sua bebida\n1) Coca\n2) Pepsi\n3) Guaraná\n4) Fanta")
    c = int(input("\nDiga sua bebida: "))

    for i in comidas:
        print("\nVocê pediu: " + comidas[a - 1] + " + " + bebidas[c-1])
        break

else:
    for i in comidas:
        print("\nVocê pediu: " + comidas[a - 1])
        break


