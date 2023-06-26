nsoma = 0
cont = 0
espaco_num = int(input('Insira um valor: '))
for ni in range(1, espaco_num):
    # print(ni, end=' ')
    if ni % 3 == 0:
        if ni % 2 != 1:
            nsoma = nsoma + ni
            cont = cont + 1

print(f'{nsoma} equivale a soma dos valores solicitados')

print(f'Existem {cont} valores "multiplos de três" dentro do range 1 à {espaco_num} ')
