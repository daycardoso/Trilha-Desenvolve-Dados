import forca
import advinhacao

print("***********************************")
print("*******Escolha o seu Jogo!*********")
print("***********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Advinhação")
    advinhacao.jogar()