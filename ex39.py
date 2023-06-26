from datetime import date
atual = date.today().year

ano_nasc = int(input('Informe o ano de nascimento: '))
idade = atual - ano_nasc

if idade < 18:
    tempo = 18 - idade
    alistamento = atual + tempo
    print(f'Ainda faltam {tempo} ano(s) para seu alistamento obrigatório')
    print(f'Seu alistamento será em {alistamento} ')

elif idade == [16, 17]:
    print('A hora do alistamento está chegando, fique atento!')

elif idade == 18:
    print('Aliste-se já, serviço militar obrigatório!')

else:
    tempo = idade - 18
    alistamento = atual + tempo
    print(f'Reservista! Você está alistado há {tempo} ano(s)')
    print(f'Seu alistamento foi feito em {alistamento} ')

