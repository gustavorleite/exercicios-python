# bases númericas
    # binários (0, 1)
    # octais (0, 1, 2, 3, 4, 5, 6, 7)
    # hexadec. (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)

dec = int(input('nº: '))

print('''Conversor de bases númericas decimais. 
REGRAS:
      [1] Binário 
      [2] Octais 
      [3] Hexadecimais ''')

opt = int(input('ESCOLHA ENTRE 1 | 2 | 3: '))

if opt == 1:
    print(bin(dec)[2:])

elif opt == 2:
    print(oct(dec)[2:])

elif opt == 3:
    print(hex(dec)[2:])

else:
    print('ERROR: OPÇÃO INVÁLIDA')








