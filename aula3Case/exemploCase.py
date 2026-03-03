opc = int(input("\n 1 - Sacar \n 2 - Extrato \n 3 - Sair \n Escolha a opção: "))
 
match opc:
    case 1:
        print("Você escolheu a opção Sacar")
        valor = float(input("Digite o valor do saque: "))
        print(f"Sacando da sua conta o valor de R${valor}")
    case 2:
        print("Você escolheu a opção Extrato")
        dias = int(input("Digite a qunantidade de dias: "))
        print(f"Retirando o extrato de {dias} dias...")
    case 3:
        print("Obrigado por usar o sistema, volte sempre!")
        exit
    case _:
        print("Opção inválida1")
números = [1, 2, 3, 4, 5]
for numero in números:
    print(numero)