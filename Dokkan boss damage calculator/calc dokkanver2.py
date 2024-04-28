danoboss = 0
cellm_super = 1855000
dbsbrolyaoe_super = 840000
dbsbrolyfp_super = 1200000
omegarzstr = 952000
omegarznuke = 1575000
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
    print("Escolha seu boss:\n")
    print("1- Cell Max (Evento)")
    print("2- Broly DBS (Red Zone) (Fase AOE)")
    print("3- Broly DBS (Red Zone) (Fase final)")
    print("4- Omega Shenron (Red Zone) (Fase STR)")
    print("5- Omega Shenron (Red Zone) (Fase final)")

    choice = int(input("Escolha o boss: "))

    if choice == 1:
        danoboss = danoboss + cellm_super
        print("\nCell Max\n\nDano do Super Attack: 1.855.000\n")

    elif choice == 2:
        danoboss = danoboss + dbsbrolyaoe_super
        print("\nBroly DBS (Fase AOE)\n\nDano do Super Attack: 840.000\n")

    elif choice == 3:
        danoboss = danoboss + dbsbrolyfp_super
        print("\nBroly DBS (Full Power)\n\nDano do Super Attack: 1.200.000\n")

    elif choice == 4:
        danoboss = danoboss + omegarzstr
        print("\nOmega Shenron (Red Zone) STR\n\nDano do Super Attack: 952.000\n")

    elif choice == 5:
        danoboss = danoboss + omegarznuke
        print("\nOmega Shenron (Red Zone) INT\n\nDano do Super Attack: 1.575.000\n")

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

    final = input("Deseja calcular outra coisa? (S/N): ")

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