s = float(input('Insira o valor do seu salário atual: R$'))

if s <= 1250:
    print('Com o aumento previsto em 15% seu salário será de R${:.2f}'.format(s+(s*0.15)))
else:
    print('Com o aumento previsto em 10%, seu salário será de R${:.2f}'.format(s+(s*0.10)))
