numeros_pares = []
numeros_impares = []
for i in range(10):
    numero = int(input(f'Digite o número {i + 1}: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        print(f'Número {numero} é ímpar.')
        print(f'Número {numero} é par.')
        print(f'Números pares digitados: {numeros_pares}')
        print(f'Números ímpares digitados: {numeros_impares}')
        