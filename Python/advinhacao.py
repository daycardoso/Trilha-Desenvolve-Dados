import random
def jogar():
    print("***********************************")

    print("Bem vindo ao Jogo de Advinhação!")
    print("***********************************")

    total_de_tentativas = 0

    numero_secreto = random.randint(0, 101)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute<1 or chute>100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue
        
        acertou = (numero_secreto) == chute
        maior = chute > (numero_secreto)
        menor = chute < (numero_secreto)


        if (acertou):

            print("Você acertou!")

            break

        else:

            if (maior):

                print("Você errou! O seu chute foi maior que o número secreto.")

            elif (menor):

                print("Você errou! O seu chute foi menor que o número secreto.")


    print("Fim do jogo")
    
if __name__ == "__main__":
    jogar()
