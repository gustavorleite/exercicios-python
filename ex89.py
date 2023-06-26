lst = []

while True:
    nome = str(input('NOME: ')).upper()
    nota1 = float(input('NOTA P1: '))
    nota2 = float(input('NOTA P2: '))
    media = (nota1 + nota2) / 2
    lst.append([[nome], [nota1, nota2], [media]])

    continuar = str(input('DESEJA INSERIR MAIS NOTAS? [S/N]: ')).strip().upper()
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        break

print('-' * 50)
#print(f'{"NOME":<10}{"NOTAS (P1)(P2)":>10}{"MÉDIA":>10}')
# MINHA SOLUÇAO
#for r in range(0, len(lst)):
#    print(f'{lst[r]}')

for i, a in enumerate(lst):
    print(f'{i:<4}{a[0]:<10]}{a[2]:>8.1f}')