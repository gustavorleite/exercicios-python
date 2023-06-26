km = float(input('Quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias: '))
pkm = 0.15 * km
pdias = 60 * dias
pfinal = pkm+pdias
print('O valor a ser pago no aluguel do carro será de: {:.2f}R$'.format (pfinal))
