danoboss = 0
cellm_super = 1855000
dbsbrolyaoe_super = 840000
dbsbrolyfp_super = 1200000
omegarzstr = 952000
omegarznuke = 1575000
mcc_super = 1956500
intfz_super = 1250000
phyfz_super = 2275000
teqfz_super = 2100000
intsstrunks = 1740000
physstrunks = 2345000
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
    print("1- Cell Max TEQ (Fearsome activation cell max)")
    print("2- Broly DBS (Red Zone Movie bosses) (Fase AOE)")
    print("3- Broly DBS (Red Zone Movie bosses) (Fase final)")
    print("4- Omega Shenron (Red Zone GT bosses) (Fase STR)")
    print("5- Omega Shenron (Red Zone GT bosses) (Fase final)")
    print("6- Metal Cooler Core (Red Zone Wicked bloodline)")
    print("7- Zamasu fusão INT (Red Zone Dismal future)")
    print("8- Zamasu fusão PHY (Red Zone Dismal future)")
    print("9- Zamasu fusão TEQ (Divine Wrath and Mortal Will)")
    print("10- Trunks SSJ (Futuro) INT (Divine Wrath and Mortal Will)")
    print("11- Trunks SSJ (Futuro) PHY (Divine Wrath and Mortal Will)")

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

    elif choice == 6:
        danoboss = danoboss + mcc_super
        print("\nMetal Cooler Core (Red Zone) PHY\n\nDano do Super Attack: 1.505.000 (aumenta o dano em 30%, o tornando 1.956.500)\n")

    elif choice == 7:
        danoboss = danoboss + intfz_super
        print("\nZamasu Fusão (Red Zone) INT\n\nDano do Super Attack: 1.250.000\n")

    elif choice == 8:
        danoboss = danoboss + phyfz_super
        print("\nZamasu Fusão (Red Zone) PHY\n\nDano do Super Attack: 1.750.000 (aumenta o dano em 30%, o tornando 2.275.000)\n")

    elif choice == 9:
        danoboss = danoboss + teqfz_super
        print("\nZamasu Fusão TEQ\n\nDano do Super Attack: 2.100.000\n")

    elif choice == 10:
        danoboss = danoboss + teqfz_super
        print("\nTrunks SSJ (Futuro) INT\n\nDano do Super Attack: 1.740.000\n")

    elif choice == 11:
        danoboss = danoboss + teqfz_super
        print("\nTrunks SSJ (Futuro) PHY\n\nDano do Super Attack: 2.345.000\n")

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