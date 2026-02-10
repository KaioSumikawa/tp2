nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = int(input('Digite o ano atual: '))

idade = anoAtual - anoNascimento
dias = 365 * idade

print(f'Seu nome é {nome} e você viveu {dias:.2f}')