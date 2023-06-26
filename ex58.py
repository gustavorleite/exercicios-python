from random import randint

cpu = randint(0, 10)
jogador = int(input('Qual nº eu estou pensando? '))

acertou = False
palpites = 1

while not acertou:
    palpites += 1
    jogador = int(input('Tente novamente: '))

    if jogador == cpu:
        acertou = True

    else:
        if jogador < cpu:
            print('Tente um nº MAIOR')
        elif jogador > cpu:
            print('Tente um nº MENOR')

if palpites == 1:
    print(f'Parabéns! Você adivinhou em sua {palpites}ª tentativa')

else:
    print(f'Parabéns! Você acertou após {palpites} tentativas!')