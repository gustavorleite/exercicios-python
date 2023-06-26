# P.A 3.0

print('Gerador de P.A')

p_termo = int(input('Insira o primeiro termo: '))
razao = int(input('Razão da P.A: '))
mais_termo2 = 0
lst = []

cont = 1

while cont <= 10:
    print(f'{p_termo} >>> ', end='')
    p_termo += razao
    cont += 1

else:
    mais_termo2 = int(input('\nInsira mais quantos termos deseja mostrar: '))
    while mais_termo2 != 0:
        print(f'{p_termo} >>>', end='')
        p_termo += razao
        cont += mais_termo2

    if mais_termo2 == 0:
        print('OK! Finalizando Operação.')

