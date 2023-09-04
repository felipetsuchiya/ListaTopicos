def imprimir_tabuleiro(tabuleiro):
    # Esta função imprime o estado atual do tabuleiro.
    for linha in tabuleiro:
        print(" | ".join(linha))  # Imprime uma linha do tabuleiro
        print("-" * 17)  # Imprime uma linha de traços para separar as linhas

def verificar_vencedor(tabuleiro, jogador):
    tamanho = len(tabuleiro)

    # Verificar linhas e colunas
    for i in range(tamanho):
        #verifica se alguma linha ou coluna está preenchida com o símbolo do jogador
        if all(tabuleiro[i][j] == jogador for j in range(tamanho)) or all(tabuleiro[j][i] == jogador for j in range(tamanho)):
            return True

    #verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(tamanho)) or all(tabuleiro[i][tamanho - 1 - i] == jogador for i in range(tamanho)):
        # Verifica as duas diagonais (ascendente e descendente)
        return True

    return False

def criar_tabuleiro(tamanho):
    # Esta função cria um tabuleiro vazio com o tamanho especificado.
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

#Funcao principal
def jogo_da_velha():
    tamanho = 4  # Tamanho do tabuleiro (4x4)
    tabuleiro = criar_tabuleiro(tamanho)  # Cria o tabuleiro vazio com o tamanho especificado
    jogador = "X"  # Começa com o jogador X
    movimentos = 0

    print("Bem-vindo ao Jogo da Velha 4x4!")
    imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro vazio

    while movimentos < tamanho ** 2:
        linha = int(input(f"Jogador {jogador}, escolha a linha (1-{tamanho}): ")) - 1
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (1-{tamanho}): ")) - 1

        if 0 <= linha < tamanho and 0 <= coluna < tamanho and tabuleiro[linha][coluna] == " ":
            #verifica se o movimento é válido e atualiza o tabuleiro
            tabuleiro[linha][coluna] = jogador
            movimentos += 1
            imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro após o movimento

            if verificar_vencedor(tabuleiro, jogador):
                print(f"Parabéns! Jogador {jogador} venceu!")  # Verifica se o jogador venceu
                break

            jogador = "O" if jogador == "X" else "X"  # Alterna entre os jogadores
        else:
            print("Movimento inválido. Tente novamente.")

    if movimentos == tamanho ** 2:
        print("Empate! O jogo terminou em empate.")  # Verifica se o jogo terminou em empate

jogo_da_velha()
