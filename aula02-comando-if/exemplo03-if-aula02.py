import os
os.system('cls')

print('$$$ Programa de Empréstimo $$$ \n Responda(0-Não, 1-Sim)')

neg = int(input('Possui nome negativo? '))
if neg == 1:
    print('Empréstimo Negado!')
else: 
    cartass = int(input('Possui carteira assinada? '))
    if cartass == 0:
        print('Empréstimo Negado!')
    else: 
        casa = int(input('Possui casa própria? '))
        if casa == 0:
            print('Empréstimo Negado!')
        else: 
            print('Empréstimo Aprovado!')