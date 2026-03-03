import os
os.system('cls')
nomes = ['Maria', 'João', 'Paulo', 'Magali']
nome_procurado = input('Digite um nome para localizar: ')
encontrado = False
for nome in nomes:
    if nome == nome_procurado:
        print(f'Nome encontrado: {nome}')
        encontrado = True
        break
    if not encontrado:
        print('Nome não encontrado.')