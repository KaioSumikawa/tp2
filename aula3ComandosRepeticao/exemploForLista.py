#Exemplo for utilizando lista de valores pré-definida

frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    print(lista)


buscar = 'goiaba'
frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    if lista == buscar:
        print(f"Fruta Encontrada {buscar}")
        break
    else:
        print(f"Fruta não encontrada {buscar}")
