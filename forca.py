import random

def jogar():

    print("###########################")
    print("Bem Vindo ao Jogo da Forca!")
    print("###########################")
   

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo: 
        linha = linha.strip()
        palavras.append(linha)       
    
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()    
    

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute =  input("Qual Letra? ")
        chute = chute.strip().upper() # strip() uma função que remove espaço do que foi digitado

        if(chute in palavra_secreta):
            index = 0  
        for letra in palavra_secreta:
            if (chute == letra): #upper() função que transforma em maiuscula
               letras_acertadas[index] = letra
              #print("Encontrei a letra {} na posição {}".format(letra, index))
            index += 1 

        else:
            tentativas += 1

        print("jogando....")

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
         print("Você Ganhou")
    else:
         print("Você Perdeu")
    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()

