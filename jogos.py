import forca
import advinhacao2

def escolha_jogo():
    print("###########################")
    print("####Escolha o seu Jogo ####!")
    print("###########################")


print("(1)Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print ("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    advinhacao2.jogar()

if(__name__ == "__main__"):
    escolha_jogo()