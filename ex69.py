#
from time import sleep

cont_idade_18 = 0
cont_idade_f_20 = 0
cont_sexo_m = 0

while True:
    print('-' * 25)
    print('    CADASTRO PESSOAL ')
    print('-' * 25)

    idade = int(input('Insira a IDADE: '))
    if idade > 18:
        cont_idade_18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Insira o SEXO: ')).strip().upper()
        if sexo == 'M':
            cont_sexo_m += 1

        if sexo == 'F' and idade < 20:
            cont_idade_f_20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('OK! FINALIZANDO INFORMAÇÕES! ')
sleep(1)
print(f'Nº DE HOMENS = {cont_sexo_m}')                              # HOMENS
print(f'PESSOAS MAIORES (+18) = {cont_idade_18}')                   # > 18
print(f'Nº DE MULHERES MENORES DE 20 ANOS = {cont_idade_f_20}')     # F < 20