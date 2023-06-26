    # EMPRESTIMO BANCARIO

salario = float(input('Salário: R$ '))
vcasa = float(input('Valor da casa: '))
anos = int(input('Quantos anos de financiamento: '))
meses = anos * 12
prestação = vcasa / meses

    # SE O VALOR DO SALARIO FOR INFERIOR À 30% DO VALOR DA PRESTAÇÃO MENSAL O EMPRESTIMO DEVERÁ SER NEGADO

if prestação >= salario*(30/100):
       print('O emprestimo foi NEGADO')
else:
       print('O emprestimo foi CONCEDIDO')
