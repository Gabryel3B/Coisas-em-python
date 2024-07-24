def main():
    num_quest = 1
    pontua = 0

    for key in perguntas:
        print("---------------------------------------")
        print("QUESTÃO "+str(num_quest)+":")
        print(key)
        for res in respostas[num_quest -1]:
            print(res)
        resp = input("Insira sua resposta: ").upper()
        num_quest +=1

        if resp == perguntas.get(key):
            pontua +=1

    uh = extra(pontua)

    if pontua > 1 and int(uh) > 0:
        print("Sua pontuação total foi de: "+str(pontua+uh) + " pontos!")
        print("Você acertou "+str(pontua)+" de "+str(num_quest-1)+" e acertou a Questão Bônus! Parabéns!!")

    elif pontua > 1:
        print("Sua pontuação total foi de: "+str(pontua) + " pontos!")
        print("Você acertou "+str(pontua)+" de "+str(num_quest-1)+"!")

    elif pontua == 1:
        print("Sua pontuação total foi de: 1 ponto!")
        print("Você acertou " + str(pontua) + " de " + str(num_quest - 1) + "!")

    elif pontua == 0:
        print("Hmm.. parece que você não acertou nenhuma..")

def extra(valor):
    if valor >= 4:
        print("---------------------------------------")
        print("QUESTÃO BÔNUS:")
        print("Perguntabonus")  # insira qualquer questão
        for res in respostasbonus:
            print(res)
        resp = input("Insira sua resposta: ").upper()

        return 5 if resp == "A" else 0

    else:
        return 0


perguntas = {  # Coloque suas perguntas e as alternativas certas
    "Pergunta1":"A",
    "Pergunta2":"B",
    "Pergunta3":"C",
    "Pergunta4":"D",
    "Pergunta5":"E"
}

respostas = [["A - Sim","B - Não","C - Talvez","D - N sei"],  # coloque as respostas de cada pergunta
             ["A - Sim","B - Não","C - Talvez","D - N sei"],
             ["A - Sim","B - Não","C - Talvez","D - N sei"],
             ["A - Sim","B - Não","C - Talvez","D - N sei"],
             ["A - Sim","B - Não","C - Talvez","D - N sei"]]

respostasbonus = ["A - Sim","B - Não","C - Talvez","D - N sei"]  # as respostas da pergunta bônus

main()