compraTotal = int(input('Digite o valor da compra: '))
formaPagamento = int(input('Digite a forma de pagamento: 1 (à vista) 2 (débito) 3 (crédito)'))

if formaPagamento == 1:
    print('Pagamento à vista, desconto de 15%')
    desconto = compraTotal * 0.15
    valorFinal = compraTotal - desconto
    print(f'Valor final: R$ {valorFinal:.2f}')

elif formaPagamento == 2:
    print('Pagamento no débito, desconto de 10%')
    desconto = compraTotal * 0.10
    valorFinal = compraTotal - desconto
    print(f'Valor final: R$ {valorFinal:.2f}')

elif formaPagamento == 3:
    print('Pagamento no crédito, desconto de 5%')
    desconto = compraTotal * 0.05
    valorFinal = compraTotal - desconto
    print(f'Valor final: R$ {valorFinal:.2f}')