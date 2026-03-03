import os
os.system('cls')
linguagens = ['python', 'c#', 'Visual Basic', 'C++', 'Delphi', 'Cobol']
contador = 0
for linguagem in linguagens:
    if len(linguagem) > 3:
        print(linguagem)
        contador += len(linguagem)
        print(f'A quantidade de caracteres de todas as linguagens da lista é: {contador}')
