lst_pessoas = list()
lst_peso = list()

while True:
    p = lst_pessoas.append(str(input('NOME: ')))
    # lst_pessoas.append(p)

    kg = lst_peso.append(float(input('PESO (EM KG): ')))
    # lst_peso.append(kg)

    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        break

# LISTA COMPLETA DE PESSOAS
print('-='*30, '\n'
      f'A lista de nomes é: {lst_pessoas}\n'
      f'A lista de pesos é: {lst_peso}\n'
      f'Ao todo foram cadastrados {len(lst_pessoas)} pessoas'
)

print() # PULAR LINHA

dados = list()
dados.append(lst_pessoas[:])
dados.append(lst_peso[:])

# NOME E PESO DAS PESSOAS
for c in range(len(dados[0])):
    print(f'NOME:{(lst_pessoas[c])}\nPESO:{(lst_peso[c])}kg\n')

print(f'O maior peso foi de {max(lst_peso)}kg')

print(f'O menor peso foi de {min(lst_peso)}kg')



