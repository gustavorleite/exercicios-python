v = str(input('Digite sua expressão: '))
qntd = []

for simb in v:
    if simb in '(':
        qntd.append('(')
    elif simb in ')':
        if len(qntd) > 0:
            qntd.pop()
        else:
            qntd.append(')')
            break
if len(qntd) == 0:
    print('EXPRESSÃO VÁLIDA')
else:
    print('EXPRESSÃO INVÁLIDA')




