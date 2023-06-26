    # ANALISADOR COMPLETO

lista_mulheres = []
lista_mulheres_18 = 0

lista_homens = []
lista_homens_40 = 0

soma_idades = 0
soma_idades_mulheres = 0
soma_idades_homens = 0


for analisador in range(1, 4+1):
    print(f'DADOS DA {analisador}ª PESSOA')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    genero = str(input('[M/F]: ')).upper()
    soma_idades += idade
    media_idades = (soma_idades / analisador)
    if genero in 'F':
        soma_idades_mulheres += idade
        # media_idades_mulheres = (soma_idades_mulheres / )
    if genero in 'M':
        soma_idades_homens += idade
        # media_idades_homens = (soma_idades_homens / )

    if genero in 'F':
        lista_mulheres += [genero]
    if genero in 'F' and idade < 18:
        lista_mulheres_18 += 1
    else:
        if genero in 'M':
            lista_homens += [genero]
        if genero in 'M' and idade >= 40:
            lista_homens_40 += 1

print(f'A média das idades indicadas na lista é de {media_idades} anos')
print(f'Existem {len(lista_mulheres)} mulheres indicadas na lista, dessas, {lista_mulheres_18} é menor de 18 anos')
print(f'Existem {len(lista_homens)} homens na indicados na lista, desses, {lista_homens_40} é maior de 40 anos')
print(f'A soma das idades de todos os homens é de {soma_idades_homens} ') # a média entre elas é {media_idades_homens}')
print(f'A somaa das idades de todas as mulheres é de {soma_idades_mulheres} ') # a média entre elas é {media_idades_mulheres}')