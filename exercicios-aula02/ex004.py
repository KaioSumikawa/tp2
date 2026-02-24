import os
os.system('cls')

n1 = int(input('Digite um número inteiro positivo: '))

if n1 % 2 == 0:
    print(f'O número {n1} é par!')
    par = n1
    print(f'O número {n1} elevado ao quadrado é {par**2:.2f}!')
else:
    print(f'O número {n1} é ímpar!')
    impar = n1
    print(f'O número {n1} elevado ao cubo é {impar**3:.2f}!')
