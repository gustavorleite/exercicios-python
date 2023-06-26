print('=' * 30)
print('         BANCO É LIXO            ')
print('=' * 30)

saque = int(input('Insira o valor que deseja sacar: R$'))

notas_1 = saque - 1.0
notas_5 = saque // 5.0
notas_10 = saque // 10.0
notas_20 = saque // 20.0
notas_50 = saque // 50.0

while True:
    res = int(input('Deseja sacar em qual valor? '
                    '\n[R$5,00]'
                    '\n[R$10,00]'
                    '\n[R$20,00]'
                    '\n[R$50,00]'
                     '\n'))
    if res == 1:
        print(f'Você receberá {notas_1} notas de R$1')
        break
    if res == 5:
        print(f'Você receberá {notas_5} notas de R$5')
        break
    if res == 10:
        print(f'Você receberá {notas_10} notas de R$10')
        break
    if res == 20:
        print(f'Você receberá {notas_20} notas de R$20')
        break
    if res == 50:
        print(f'Você receberá {notas_50} notas de R$50')
        break