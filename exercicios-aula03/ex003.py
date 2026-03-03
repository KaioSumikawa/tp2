u = int(input('Digite a tensão em volts: '))
R = int(input('Digite a resistência em ohms: '))
i = int(input('Digite a corrente em ampéres: '))

tensao = u = R * i 
resistencia = R = u / i
corrente = i = u / R

print('Cálculo de tensões elétricas: ')
print(f'Tensão (em Volt) {tensao:.2f} ')
print(f'Resistência (em Ohm) {resistencia:.2f} ')
print(f'Corrente (em Ampére) {corrente:.2f} ')
