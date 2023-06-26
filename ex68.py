import random

par_impar = ' '
while par_impar not in 'PI':
    par_impar = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()

while True:
    J = int(input('Sua jogada: '))
    while J > 10:
        print('DIGITE UM Nº VÁLIDO [1 ~ 10]')
        J = int(input('Sua jogada: '))
    CPU = random.randint(1, 10)
    R = J + CPU
    print('-' * 30)
    print(f'Jogador escolheu: {J}\nCPU escolheu: {CPU}\n{J} + {CPU} = {R}')

    if par_impar == 'Pp':
        if R % 2 == 0:
            print('Jogador Venceu!! ')
        else:
            print('Computador Venceu!! ')
            break
    elif par_impar == 'Ii':
        if R % 2 != 0:
            print('Jogador Venceu!!')
        else:
            print('Computador Venceu!!')
break