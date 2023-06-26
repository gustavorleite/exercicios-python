    #
while True:
    t = int(input('TABUADA: ')) # Mostra resultado da multiplicaçao de 1 a 10
    if t == 0:
        break
    print('-' * 25)
    for c in range(1, 11):
        print(f' {t} x {c} = {t*c}')
    print('-' * 25)
