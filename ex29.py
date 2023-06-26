from time import sleep
V = float(input('Velocidade(km/h): '))
print('PROCESSANDO . . .')
sleep(1)
if V >= 80\
        :
    n = 7 * (V-80)
    print('VOCÊ FOI MULTADO! A VELOCIDADE MÁXIMA DA VIA É DE 80km/h ')
    print('\033[31mcusto: R${:.2f}\033[m '.format(n))
else\
        :
    print('\033[32mBoa viagem, dirija com segurança!')
