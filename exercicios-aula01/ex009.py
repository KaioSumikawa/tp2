votosBrancos = int(input('Informe quantos votos brancos: '))
nulos = int(input('Informe quantos votos nulos: '))
validos = int(input('Informe quantos votos válidos: '))

totalEleitores = votosBrancos + nulos + validos

percBrancos = (votosBrancos * 100) / totalEleitores
percNulos = (nulos * 100) / totalEleitores
percValidos = (validos * 100) / totalEleitores

print(f'Percentual votos brancos é: {percBrancos:.2f}')
print(f'Percentual votos nulos é: {percNulos:.2f}')
print(f'Percentual votos válidos é: {percValidos:.2f}')