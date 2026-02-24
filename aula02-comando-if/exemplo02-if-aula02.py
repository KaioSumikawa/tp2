#Comando para limpar a tela do terminal
import os
os.system('cls')


#Estrutura if Operadores Relacionais and = e or = ou not = negação

num1 = int(input('Digite um número: '))
num2 = int(input('Digite o outro número: '))
num3 = int(input('Digite o último número: '))

if num1 == num2 or num2 == num3 or num3 == num1:
    exit()#termina a execução do programa
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1:.2f}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2:.2f}')
else:
    print(f'O maior número é {num3:.2f}')