import os
os.system('cls')
tabuada = int(input('Digite a tabuada que deseja: '))
valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
contador = valor_inicial
while contador <= valor_final:
    resultado = tabuada * contador
    print(f'{tabuada} x {contador} = {resultado}')
    contador += 1
    