pessoas = dict()

lst_mulheres = []
lst_idade = []
lst_mmedia = []

while True:
    pessoas['nome'] = str(input('NOME: ')).capitalize()
    while True:
        pessoas['sexo'] = str(input('SEXO [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas [M] ou [F].')
    if pessoas['sexo'] in 'Ff':
        lst_mulheres.append(pessoas.copy()['nome'])
    pessoas['idade'] = int(input('IDADE: '))
    lst_idade.append(pessoas['idade'])
    media = sum(lst_idade)/(len(lst_idade))
    if pessoas['idade'] > media:
        lst_mmedia.append(pessoas.copy()['nome'])
    print()
    for k, v in pessoas.items():
        print(f'{k.capitalize()}: {v}')
    print()
    while True:
        continuar = str(input('DESEJA CONTINUAR? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por Favor, digite apenas [S] "Sim" ou [N] "Não".')
    if continuar in 'Nn':
        print()
        break
    elif continuar in 'Ss':
        print()
        continue

print(
      f'A) Foram cadastradas {len(lst_idade)} pessoas.\n'
      f'B) A média entre as idades é: {media}\n'
      f'C) São mulheres: {lst_mulheres}\n'
      f'D) Pessoas com idades acima da média: {lst_mmedia}')