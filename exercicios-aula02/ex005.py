import os
os.system('cls')

altura1 = float(input('Digite a altura da primeira pessoa: '))
altura2 = float(input('Digite a altura da segunda pessoa: '))
altura3 = float(input('Digite a altura da terceira pessoa: '))

if altura1 > altura2 and altura1 > altura3:
    print(f'A pessoa mais alta é {altura1:.2f}! A segunda pessoa mais alta é {altura2:.2f} e a terceira pessoa mais alta é {altura3:.2f}!')
elif altura2 > altura1 and altura2 > altura3:
    print(f'A pessoa mais alta é {altura2:.2f}! A segunda pessoa mais alta é {altura1:.2f} e a terceira pessoa mais alta é {altura3:.2f}!')
else:
    print(f'A pessoa mais alta é {altura3:.2f}! A segunda pessoa mais alta é {altura1:.2f} e a terceira pessoa mais alta é {altura2:.2f}!')