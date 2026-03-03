# Exemplo for append para adicionar valores a lista
 
numeros = []
 
for i in range(1,5):
    numero = int(input(f"Digite o {i}º número da lista: "))
    numeros.append(numero)
 
print(f"Lista = {numeros}")
 
print("numeros digitados: ")
for i in numeros:
    print(i)