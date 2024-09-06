def quiz_adicao():
    cont = 0
    total_perguntas = 4

    print("Sobre matemática")
    print("adição")
    print('Quanto é 2 + 6?')
    print('a) 9, b) 5, c) 8, d) 4')
    resposta = input('Digite: ')
    if resposta == "c":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("adição")  
    print("Quanto é 3 + 4?")
    print("a) 7, b) 1, c) 5, d) 2")  
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou")
        cont += 1
    else:
        print("Errou")    

    print("Sobre matemática")
    print("adição")
    print("Quanto é 4 + 5?")
    print("a) 8, b) 6, c) 5, d) 9")
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("adição")
    print("Quanto é 5 + 6?")
    print("a) 12, b) 17, c) 19, d) 11")
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou")
        cont += 1
    else:
        print("Errou")  

    percentual_acertos = (cont / total_perguntas) * 100
    percentual_erros = 100 - percentual_acertos
    print(f"\nVocê acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%\n")

def quiz_subtracao():
    cont = 0
    total_perguntas = 4

    print("Sobre matemática")
    print("subtração")
    print('Quanto é 5 - 4?')
    print('a) 1, b) 8, c) 3, d) 2')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("subtração")  
    print("Quanto é 7 - 3?")
    print("a) 9, b) 2, c) 6, d) 4")  
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou")
        cont += 1
    else:
        print("Errou") 

    print("Sobre matemática")
    print("subtração")
    print('Quanto é 9 - 6?')
    print('a) 8, b) 3, c) 7, d) 5')
    resposta = input('Digite: ')
    if resposta == "b":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("subtração")
    print('Quanto é 5 - 2?')
    print('a) 6, b) 1, c) 3, d) 7')
    resposta = input('Digite: ')
    if resposta == "c":
        print("Acertou")
        cont += 1
    else:
        print("Errou")    

    percentual_acertos = (cont / total_perguntas) * 100
    percentual_erros = 100 - percentual_acertos
    print(f"\nVocê acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%\n")

def quiz_multiplicacao():
    cont = 0
    total_perguntas = 4

    print("Sobre matemática")
    print("multiplicação")
    print('Quanto é 4 x 5?')
    print('a) 50, b) 20, c) 26, d) 45')
    resposta = input('Digite: ')
    if resposta == "b":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("multiplicação")
    print('Quanto é 3 x 8?')
    print('a) 24, b) 43, c) 14, d) 18')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou")
        cont += 1
    else:
        print("Errou")

    print("Sobre matemática")
    print("multiplicação")
    print('Quanto é 6 x 7?')
    print('a) 37, b) 28, c) 53, d) 42')
    resposta = input('Digite: ')
    if resposta == "d":
        print("Acertou")
        cont += 1
    else:
        print("Errou")    

    print("Sobre matemática")
    print("multiplicação")
    print('Quanto é 5 x 5?')
    print('a) 25, b) 55, c) 15, d) 45')
    resposta = input('Digite: ')
    if resposta == "a":
        print("Acertou")
        cont += 1
    else:
        print("Errou")    

    percentual_acertos = (cont / total_perguntas) * 100
    percentual_erros = 100 - percentual_acertos
    print(f"\Você acertou {cont} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%\n")

def menu():
    while True:
        print("Menu:")
        print("Digite 1 para responder o quiz de adição")
        print("Digite 2 para responder o quiz de subtração")
        print("Digite 3 para responder o quiz de multiplicação")
        print("Digite 4 para sair do programa")
        
        opcao = input('Digite sua opção: ')
        
        if opcao == "1":
            quiz_adicao()
        elif opcao == "2":
            quiz_subtracao()
        elif opcao == "3":
            quiz_multiplicacao()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

menu()