import os
os.system('cls')
tabuada = int(input('Digite a tabuada que deseja: '))
contador = 1
while contador <= 10:
    resultado = tabuada * contador
    print(f'{tabuada} x {contador} = {resultado}')
    contador += 1
    