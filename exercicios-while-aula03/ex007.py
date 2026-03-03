import os
os.system('cls')
nomes = []
for i in range(7):
    nome = input(f'Digite o nome {i + 1}: ')
    nomes.append(nome)
    print(f'Nome armazenado: {nome} - Posição na lista: {i}')
    