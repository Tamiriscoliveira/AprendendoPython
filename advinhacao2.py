#importação das bibliotecas necessárias
import random   #biblioteca random server para número aleatórios

def jogar():

   print("*********************************")
   print("Bem vindo ao jogo de Adivinhação!")
   print("*********************************")

#variaveis
numero_secreto = random.randrange(1,101)  #função randon gera número entre 0.0 1.1
total_de_tentativas = 0
pontos = 100

#nivel
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Dificil")

nivel = int(input("Defina o nível"))

#tentativas
if(nivel ==1):
    total_de_tentativas = 20
elif(nivel == 2):
     total_de_tentativas = 10
else:
    total_de_tentativas = 5

#laço
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos

print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()