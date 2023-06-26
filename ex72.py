tupla_n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

n = int(input('Digite um nº entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um nº entre 0 - 20: '))
    if 0 <= n <= 20:
        break

print(f'A tupla possui {len(tupla_n)} itens \nVocê indicou o {n+1}ª item, escrito por extenso é o nº {tupla_n[n]} ')