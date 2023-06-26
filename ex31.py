print('Calcule o preço de sua viagem a partir da distância')
p = float(input('Insira a distância a percorrer (em km): '))
if p <= 200:
    p1 = 0.50 * p
    print('O preço final até seu destino é: {}'.format (p1))
else:
    p2 = 0.45 * p
    print(f'O preço final até seu destino é: {p2}')
