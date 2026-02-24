import math
altura = float(input('Digite a altura: '))
r = float(input('Digite o raio: '))
volume = math.pi * (r * r) * altura
print(f'O volume da lata é {volume:.2f}')