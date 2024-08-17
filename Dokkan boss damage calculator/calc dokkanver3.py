from bosslist import bosslist

danoboss = 0
def selecsitu():
    print("Em qual situação seu personagem está?")
    print("1- Desvantagem de cor, Mesma classe")
    print("2- Desvantagem de cor, Classe oposta")
    print("3- Neutro, Mesma classe")
    print("4- Neutro, Classe oposta")
    print("5- Vantagem de cor, Mesma classe")
    print("6- Vantagem de cor, Classe oposta")

print("Calculador de defesa do Dokkan (aproximado)\n")

while True:
    lista = []
    count = 1
    print("Escolha seu boss:\n")
    for i in bosslist.keys():
        lista.append(i)
        print(str(count)+"- "+i)
        count +=1

    choice = int(input("Escolha o boss: "))

    if choice > 0:
        danoboss = danoboss + bosslist[lista[choice-1]]
        print("Dano do Super Attack: "+str(danoboss))

    desvmesm = danoboss * 1.25
    desvdiff = danoboss * 1.5
    neutmesm = danoboss * 1
    neutdiff = danoboss * 1.15
    vantamesm = danoboss * 0.9
    vantadiff = danoboss * 1

    df = float(input("Insira sua defesa: "))
    print("\nSeu personagem possui defesa ativa/guard? (S/N)")
    gua = input("R: ")
    selecsitu()
    situa = int(input("R: "))
    print("Seu personagem possui redução de dano? Se sim, quantos %? (Favor escolher um valor de 1-100)")
    dr = int(input("Obs: caso não tenha, responda 0: "))

    danos = ["ignore isso",desvmesm,desvdiff,neutmesm,neutdiff,vantamesm,vantadiff]
    guard_value = 0
    drper = dr / 100
    resul = 0

    if gua == "S":
        guard_value = guard_value + 0.5

    resul = resul + (danos[situa] - (danos[situa] * drper) - (danos[situa] * guard_value) - df)

    if resul <= 0:
        print("Dois digitos, brabo.")

    elif resul > 0:
        print("Dano que você receberá: " + str(resul))

    if resul < 300000:
        print("\nVocê tankou bem!")

    elif resul > 300000 and resul < 600000:
        print("\nVai estar vivendo por aparelhos.")

    elif resul > 600000:
        print("\nVocê muito provavelmente morreu, F.")

    final = input("Deseja calcular outra coisa? (S/N): ").upper()

    if final == "S":
        guard_value = 0
        drper = 0
        resul = 0
        df = 0
        danoboss = 0
        continue

    else:
        print("Até a próxima!")
        break