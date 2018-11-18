soma = lambda number1, number2: number1 + number2
subtracao = lambda number1, number2: number1 - number2
divisao = lambda number1, number2: number1 / number2
multiplicacao = lambda number1, number2: number1 * number2

while (True) :
    operation = int(input('Coloque o numero da operação que você deseja fazer. \n 1 - Soma\n 2 - Subtracao \n 3 - Divisão \n 4 - Multiplicação\n'))
    if (operation in range(0, 5)) :
        break
    print('Escolha inválida, tente novamente')

number1 = int(input('Digite o primeiro numero '))
number2 = int(input('Digite o segundo numero '))

if (operation == 1) :
    print(soma(number1, number2))
if (operation == 2) :
    print(subtracao(number1, number2))
if (operation == 3) :
    print(divisao(number1, number2))
if (operation == 4) :
    print(multiplicacao(number1, number2))
