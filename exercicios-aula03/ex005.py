categoria = str(input('Digite sua categoria (A, B, C): '))
salario = int(input('Digite seu salário: '))

if categoria == 'A': 
    aumento = salario * 0.10
    salarioFinal = salario + aumento
    print(f'Seu salário atual é {salario} e com aumento será {salarioFinal}')
elif categoria == 'B':
    aumento = salario * 0.15
    salarioFinal = salario + aumento
    print(f'Seu salário atual é {salario} e com aumento será {salarioFinal}')
elif categoria == 'C':
    aumento = salario * 0.20
    salarioFinal = salario + aumento
    print(f'Seu salário atual é {salario} e com aumento será {salarioFinal}')