# Calculadora em Python
def imprime():
    print("\n******************* Calculadora em Python *******************")

imprime()

def menu():
    while True:

        print("Escolha uma das opções: ")
        print("\n")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao_escolhida = int(input())

        if opcao_escolhida == 1:
            calculo_adicao()
        if opcao_escolhida == 2:
            calculo_subtracao()
        if opcao_escolhida == 3:
            calculo_multiplicacao()
        if opcao_escolhida == 4:
            calculo_divisao()
        if opcao_escolhida == 5:
            break
def calculo_adicao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 + n2

    print("\n")
    print("O valor somado foi de:", resultado)
    print("\n")
    imprime()


def calculo_subtracao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 - n2

    print("\n")
    print("O valor subtraído foi de:", resultado)
    print("\n")
    imprime()

def calculo_multiplicacao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 * n2

    print("\n")
    print("O valor multiplicado foi de: ", resultado)
    print("\n")
    imprime()

def calculo_divisao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if n2 != 0:
        resultado = n1 / n2

        print("\n")
        print("O valor dividido foi de: ", resultado)
        print("\n")
        imprime()

    else:

        print("\n")
        print("Não é possivel dividir por zero")
        print("\n")
        imprime()

menu()