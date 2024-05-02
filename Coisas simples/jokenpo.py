import random

escolhas = ["Pedra", "Papel", "Tesoura"]
score = 0

print("Isso é um jogo de jokenpô e vc sabe jogar isso.")

while True:
    print("Escolha o número que corresponde a oq vc irá usar")
    pick = int(input("1- Pedra\n"
                 "2- Papel\n"
                 "3- Tesoura\n"
                 "Escolha sua jogada: "))

    player = escolhas[pick -1]

    cpu = random.choice(escolhas)

    if player == cpu:
        print("\nAmbos escolheram "+player+"! Empate!")

    elif player == "Pedra" and cpu == "Tesoura":
        print("\nVocê escolheu "+player+" e a cpu escolheu "+cpu+"! Você ganhou!")
        score+=1

    elif player == "Papel" and cpu == "Pedra":
        print("\nVocê escolheu "+player+" e a cpu escolheu "+cpu+"! Você ganhou!")
        score+=1

    elif player == "Tesoura" and cpu == "Papel":
        print("\nVocê escolheu "+player+" e a cpu escolheu "+cpu+"! Você ganhou!")
        score+=1

    else:
        print("\nA cpu escolheu "+cpu+"! Você perdeu!")

    final = input("\nQuer jogar de novo? (S/N): ").upper()

    if final == "S":
        continue

    else:
        print("Sua pontuação foi de: "+str(score)+"!")
        score = 0
        print("Até a próxima!")
        break