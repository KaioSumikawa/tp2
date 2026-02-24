import os
os.system('cls')

rg = input('Digite seu RG: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_entrou_empresa = int(input('Digite o ano que entrou na empresa: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - ano_nascimento
tempo_empresa = ano_atual - ano_entrou_empresa

if idade >= 65 or tempo_empresa >= 30 or (idade >= 60 and tempo_empresa >= 25):
    print(f'Funcionário com RG {rg} pode se aposentar!')
else:
    print(f'Funcionário com RG {rg} não pode se aposentar!')
    