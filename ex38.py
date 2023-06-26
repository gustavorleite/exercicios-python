primeiro = input('Insira o primeiro valor: ')
segundo = input('Insira o segundo valor: ')

if primeiro > segundo:
    print('O primeiro valor é MAIOR')

elif segundo > primeiro:
    print('O segundo valor é MAIOR')

else:
    primeiro = segundo
    print('Não existe valor maior, ambos são IGUAIS')