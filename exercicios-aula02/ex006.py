import os
os.system('cls')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

opcao = int(input("Escolha a opção que deseja: \n 1 - Média Ponderada \n 2 - Quadrado da soma \n 3 - Cubo do menor número \n Digite o número da opção desejada: "))
 
if opcao == 1:
    media_ponderada = (n1 * 2 + n2 * 3) / 5
    print(f"A média ponderada é: {media_ponderada}")
elif opcao == 2:
    quadrado_soma = (n1 + n2) ** 2
    print(f"O quadrado da soma é: {quadrado_soma}")
elif opcao == 3:
    menor_numero = min(n1, n2)
    cubo_menor = menor_numero ** 3
    print(f"O cubo do menor número é: {cubo_menor}")
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")