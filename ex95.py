# att EX93
aproveitamento = dict()
lstg = []
lstp = []
lstn = []
lst_geral = []

while True:
    aproveitamento.clear()

    nome = aproveitamento['Jogador'] = str(input('NOME: ')).capitalize()
    lstn.append(nome)

    partidas = aproveitamento['Partidas'] = int(input('PARTIDAS: '))
    lstp.append(partidas)

    lstg.clear()
    for p in range(0, partidas):
        lstg.append(int(input(f'SALDO DE GOLS NA {p+1}º PARTIDA? ')))
    aproveitamento['Gols'] = lstg[:]


    lst_geral.append(aproveitamento.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N]: '))
        if continuar in 'sSnN':
            break
        print('ERRO! RESPOSTA INVÁLIDA.')
    if continuar in 'Nn':
        break
print()
# noinspection NonAsciiCharacters
for cabeçalho in aproveitamento.keys():
    print(f'{cabeçalho:>15}', end='')
print('\n', '-' * 50)
for k, v in enumerate(lst_geral):
    print(f'{k}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
