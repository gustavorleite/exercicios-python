    # MAIOR E MENOR DA SEQUÊNCIA

lista = []

for p in range(1, 5+1):
    peso_pessoas = float(input(f'Insira o peso (em kg) da {p}ª pessoa: '))
    lista = lista + [peso_pessoas] # adiciona o peso de cada pessoa à lista
print()

# print(lista)

print(f'O MAIOR peso foi de {max(lista)}') # max.lista = maior valor da lista
print(f'O MENOR peso foi de {min(lista)}') # min.lista = menor valor da lista