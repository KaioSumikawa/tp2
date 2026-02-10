salario = float(input('Digite seu salário: '))
porc = float(input('Digite seu percentual de aumento: '))
ns = (salario * porc) / 100 + salario
print(f'Seu novo salário é {ns:.2f}')