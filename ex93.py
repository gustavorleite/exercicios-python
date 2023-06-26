aproveitamento = dict()

lstg = []
lstp = []
lst_pg = []

#while True:
aproveitamento.clear()

nome = aproveitamento['Jogador'] = str(input('NOME: ')).capitalize()
partidas = aproveitamento['Partidas'] = int(input('PARTIDAS: '))
lstp.append(partidas)
for p in range(0, partidas):
    gols = int(input(f'SALDO DE GOLS NA {p+1}º PARTIDA? '))
    lstg.append(gols)
    aproveitamento['Gols'] = lstg[:]
lst_pg = lstp, lstg

print(f'{aproveitamento["Jogador"]} fez um total de {sum(lstg)} gols no campeonato ')

print('-'*50) #linha

print(aproveitamento)

print('-'*50)


for k, v in aproveitamento.items():
    print(f'{k}: {v}')

print('-'*50)

print(f'O JOGADOR REALIZOU {partidas} PARTIDAS')
for p, g in enumerate(aproveitamento['Gols']):
    print(f'Na {p+1}º partida, {aproveitamento["Jogador"]} fez {g} Gols ')




#continuar = str(input('Deseja continuar? [S/N]: '))
#if continuar in 'nN':
#    break
#elif continuar in 'sS':
#    continue