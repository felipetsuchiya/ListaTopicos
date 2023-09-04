### TERMO
import random

# Le o arquivo
def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha

#Lista para gerar só com 5 letras que é como funciona no termo
def gera_lista_n_letras(lista, n):
    return [x for x in lista if len(x) == n]

#Compara a palavra secreta com o palpite e troca as cores
def verificar_palpite(palavra_secreta, palpite):
    resultado = []
    for i in range(len(palavra_secreta)):
        if palpite[i] == palavra_secreta[i]:
            resultado.append("\033[92m" + palpite[i] + "\033[0m")  # Letra na posição correta (verde)
        elif palpite[i] in palavra_secreta:
            resultado.append("\033[93m" + palpite[i] + "\033[0m")  # Letra na palavra, mas na posição errada (amarelo)
        else:
            resultado.append("\033[30m" + palpite[i] + "\033[0m")  # Letra não está na palavra (preto)
    return resultado


# início do programa
def termo():
    chance = 0
    l1 = '_ _ _ _ _'
    l2 = '_ _ _ _ _'
    l3 = '_ _ _ _ _'
    l4 = '_ _ _ _ _'
    l5 = '_ _ _ _ _'
    l6 = '_ _ _ _ _'
    lm = [l1, l2, l3, l4, l5, l6]

    palavras = le_arquivo('lista_palavras.txt')
    lista_n = gera_lista_n_letras(palavras, 5)
    palavra_secreta = random.choice(lista_n)
    print(palavra_secreta)

    while(chance < 7):

        # Lista das tentativas
        print(f"{lm[0]}")
        print(f"{lm[1]}")
        print(f"{lm[2]}")
        print(f"{lm[3]}")
        print(f"{lm[4]}")
        print(f"{lm[5]}")
       
        #Palpite
        palpite = input('Digite uma palavra: ')

        if(len(palpite) != 5):
            print("A palavra pode conter somente 5 letras")
        else:
            #verifica a palavra com o palpite e faz a troca de cores
            resultado = verificar_palpite(palavra_secreta, palpite)

            #Troca os _ pelas palavras palpitadas
            lm[chance] = " ".join(resultado)

            chance += 1

        if(palavra_secreta == palpite):
            print(f"{lm[0]}")
            print(f"{lm[1]}")
            print(f"{lm[2]}")
            print(f"{lm[3]}")
            print(f"{lm[4]}")
            print(f"{lm[5]}")
            print(f"Voce conseguiu resolver em {chance} tentativas!!!")
            break
        elif(chance == 6):
            print(f"{lm[0]}")
            print(f"{lm[1]}")
            print(f"{lm[2]}")
            print(f"{lm[3]}")
            print(f"{lm[4]}")
            print(f"{lm[5]}")
            print(f"Voce não conseguiu resolver em {chance} tentativas!!!")
            break
        else:
            continue


termo()
