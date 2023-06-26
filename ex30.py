n = int(input('Insira um nº: '))

# cor = {'verde':'\033[0;30;42m' ,
#       'vermelha': '\033[0;30;41m'}

if n == [0, 2, 4, 6, 8]:
    print('O nº{} é \033[30;42mPAR\033[m'.format(n))
else:
    print('O nº{} é \033[;30;41mIMPAR\033[m'.format(n))

