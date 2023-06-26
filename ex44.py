    #

print('-=' *10, 'SUL AMERICANAS BAR', '-=' *10)
preço = float(input('Total a pagar: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/pix
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pag = int(input('Escolha sua forma de pagamento: '))


if pag == 1:
    print(f'Valor a pagar: {preço - (preço * (10 / 100))}')

elif pag == 2:
    print(f'Valor a pagar: {preço - (preço * (5/100))}')

elif pag == 3:
    print(f'Valor a pagar: {preço/2} em 2x sem juros')

else:
    parcela = int(input('nº de parcelamentos: '))
    total = preço + (preço * (20 / 100))
    print(f'Valor a pagar: {total/parcela}')

    #