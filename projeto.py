# Função do quiz de adição
def quiz_adicao():
    cont = 0  # Contador de acertos
    total_perguntas = 4  # Número total de perguntas

    print("Quiz de adição")  # Inicia o quiz de adição
    print("Quanto é 2 + 6?")  # Primeira pergunta
    print('a) 9, b) 5, c) 8, d) 4')  # Opções
    resposta = input('Digite: ')  # Usuário insere a resposta
    if resposta == "c":  # Verifica se a resposta está correta
        print("Acertou!")  # Mensagem de acerto
        cont += 1  # Incrementa o contador de acertos
    else:
        print("Errou!")  # Mensagem de erro

    # Repetição do processo para outras perguntas
    print("Quanto é 3 + 4?")
    print("a) 7, b) 1, c) 5, d) 2")
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print("Quanto é 4 + 5?")
    print("a) 8, b) 6, c) 5, d) 9")
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print("Quanto é 5 + 6?")
    print("a) 12, b) 17, c) 19, d) 11")
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    # Exibe o resultado final
    print(f"\nVocê acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {(cont / total_perguntas) * 100:.2f}%")  # Calcula o percentual de acertos

# Função do quiz de subtração (seguindo a mesma lógica)
def quiz_subtracao():
    cont = 0
    total_perguntas = 4

    print("Quiz de subtração")
    print('Quanto é 5 - 4?')
    print('a) 1, b) 8, c) 3, d) 2')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print("Quanto é 7 - 3?")
    print("a) 9, b) 2, c) 6, d) 4")
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print('Quanto é 9 - 6?')
    print('a) 8, b) 3, c) 7, d) 5')
    resposta = input('Digite: ')
    if resposta == "b":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print('Quanto é 5 - 2?')
    print('a) 6, b) 1, c) 3, d) 7')
    resposta = input('Digite: ')
    if resposta == "c":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print(f"\nVocê acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {(cont / total_perguntas) * 100:.2f}%")

# Função do quiz de multiplicação (mesma lógica)
def quiz_multiplicacao():
    cont = 0
    total_perguntas = 4

    print("Quiz de multiplicação")
    print('Quanto é 4 x 5?')
    print('a) 50, b) 20, c) 26, d) 45')
    resposta = input('Digite: ')
    if resposta == "b":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print('Quanto é 3 x 8?')
    print('a) 24, b) 43, c) 14, d) 18')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print('Quanto é 6 x 7?')
    print('a) 37, b) 28, c) 53, d) 42')
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print('Quanto é 5 x 5?')
    print('a) 25, b) 55, c) 15, d) 45')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou!")
        cont += 1
    else:
        print("Errou!")

    print(f"\nVocê acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {(cont / total_perguntas) * 100:.2f}%")

# Função do menu principal
def menu():
    while True:
        print("Menu:")  # Exibe o menu
        print("1 - Quiz de adição")
        print("2 - Quiz de subtração")
        print("3 - Quiz de multiplicação")
        print("4 - Sair")

        opcao = input('Digite sua opção: ')  # Usuário escolhe a opção

        # Dependendo da opção escolhida, chama a função correspondente
        if opcao == "1":
            quiz_adicao()  # Chama o quiz de adição
        elif opcao == "2":
            quiz_subtracao()  # Chama o quiz de subtração
        elif opcao == "3":
            quiz_multiplicacao()  # Chama o quiz de multiplicação
        elif opcao == "4":
            print("Saindo do programa.")  # Encerra o programa
            break
        else:
            print("Opção inválida. Tente novamente.")  # Validação de entrada

# Chama o menu principal
menu()
