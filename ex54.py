from datetime import date
data = date.today().year

total_maiores = 0
total_menores = 0

for pessoa in range(1, 8):
    nascimento = int(input(f'Insira o ano de nascimento da {pessoa}ª Pessoa: '))
    idade = (data - nascimento)
    if idade >= 18:
        total_maiores += 1
        # print('GRUPO +18 ANOS')
    elif nascimento > data:
        print('Insira uma data válida')
        continue
    else:
        total_menores += 1
        # print('GRUPO MENOR')
print(f'TOTAL DE MAIORES (+18) FOI: {total_maiores}')
print(f'TOTAL DE MENORES (-18) FOI: {total_menores}')