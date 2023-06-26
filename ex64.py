print('Para executar o programa digita a quantidade de nº desejada, p/ parar digite 999')

n = 0
s = 0
while True:
    n = int(input('Digite um nº: '))

    if n == 999:
        break

    s += n

parar = input('Deseja parar? [S/N]: ')
if parar == 's'.strip():
    print(f'A soma dos números digitados equivale a {s} ')
