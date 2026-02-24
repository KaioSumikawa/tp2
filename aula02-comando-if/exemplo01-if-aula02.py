#Exemplo Estrutura condicional IF - Média de notas

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
nome = input("Digite o nome do aluno: ")

media = (n1 + n2) / 2

#comando if 
if media >= 6.0:
    print(f"Aprovado! A média é: {media:.2f}")
elif media >= 5.0 and media < 6.0:
    print(f"Exame! A média é: {media:.2f}")
else:
    print(f"Reprovado! A média é: {media:.2f}")