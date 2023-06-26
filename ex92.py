from datetime import datetime

ctps = dict()
ano_atual = datetime.now().year

# while True:
ctps['nome'] = str(input('NOME: ')).capitalize()
nasc = int(input('ANO DE NASCIMENTO: '))
ctps['idade'] = ano_atual - nasc
ctps['digitos'] = int(input('Nº CTPS (0 = NÃO POSSUI): '))
if ctps['digitos'] != 0:
    ctps['contrato'] = int(input('ANO DE CONTRATAÇÃO: '))
    ctps['salario'] = int(input('SALÁRIO (EM R$): '))
    ctps['aposentadoria'] = 65 - ctps['idade'] #criterio idade
    ctps['aposentadoria'] = ctps['contrato'] + 35 #criterio de contribuiçao
#    break
print()

for k, v in ctps.items():
    print(f'{k}: {v}')
