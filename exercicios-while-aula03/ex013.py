import os
os.system('cls')
contador = 1
while contador <= 15:
    nome = input('Digite o nome do funcionário: ')
    sexo = input('Digite o sexo do funcionário (M/F): ').upper()
    if sexo == 'M':
        print(f'O funcionário {nome} necessita fazer o exame.')
    elif sexo == 'F':
        print(f'O funcionário {nome} não necessita fazer o exame.')
    else:
        print('Sexo digitado incorretamente!')
    contador += 1