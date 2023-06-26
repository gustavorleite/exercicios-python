
boletim = {}

#while True:
boletim['NOME'] = str(input('NOME: ')).upper()
boletim['NOTA P1'] = float(input('NOTA P1: '))
boletim['NOTA P2'] = float(input('NOTA P2: '))
boletim['MEDIA'] = (boletim['NOTA P1'] + boletim['NOTA P2']) / 2
if boletim['MEDIA'] >= 6:
    boletim['SITUAÇAO'] = 'Aprovado!!'
elif boletim['MEDIA'] >= 3.5 < 6:
    boletim['SITUAÇAO'] = f'{boletim["NOME"]} está em Recuperação'
else:
    boletim['SITUAÇAO'] = 'Reprovado...'
    #continuar = str(input('Deseja Continuar: [S/N] '))
    #if continuar in 'Nn':
        #break
print('-' * 50)
for k, v in boletim.items(): #key e value
    print(f'{k}: {v}')
print()

#print(f'{lst_aprovados}'
    #f'\nSITUAÇÃO: APROVADO(S)')

#print()

#print(f'{lst_reprovados}'
    #f'\nSITUAÇÃO: REPROVADO(S)')
