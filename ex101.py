def voto(idade):
    from datetime import date
    atual = date.today().year
    idd = atual - idade
    print(f'Você possui {idd} anos.')
    if idd >= 18 and idd < 65:
        return f'voto Obrigatório'
    elif idd >= 16 or idd > 65:
        return f'voto Opcional'
    else:
        return f'voto NEGADO'

#pp
nasc = int(input('Insira o ano de nasc.: '))
print(voto(nasc))
