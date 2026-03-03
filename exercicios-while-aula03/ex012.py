import os
os.system('cls')
linguagens = ['python', 'c#', 'visual basic', 'c++', 'delphi', 'cobol', 'clipper', 'php', 'java']
linguagem = input('Digite o nome de uma linguagem: ').lower()
if linguagem in linguagens:
    print(f'A linguagem {linguagem} está na lista!')
else:
    print(f'A linguagem {linguagem} não está na lista!')
