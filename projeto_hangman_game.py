            # Desenvolvimento de Game em Linguagem Python - Versão 2

import random

from os import system, name

def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

def display_hangman(chances):

    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

                                # Função do jogo
def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    
                               # Lista de palavras para o jogo
        
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'uva']
    
                               # Escolha aleatoria de palavra chave
    palavra = random.choice(palavras)
    
                               # Lista  de letras  da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
                                # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
    
                                # Número de chances
    chances = 6
    
                                # Lista para as letras digitadas
    letras_tentativas = []
    
                                # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        tentativa = input("\nDigite uma letra: ")
        
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)
        
        if tentativa in lista_letras_palavras:
            
            print("Você acertou a letra!")

            for indice in range(len(lista_letras_palavras)):

                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            # Decremento
            chances -= 1
    
    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))


# Bloco main
if __name__ == "__main__":
    game()


