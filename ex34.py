print('Apresente os números em qualquer ordem')
num1 = int(input("nº1: "))
num2 = int(input('nº2: '))
num3 = int(input('nº3: '))

# str(input('nº1 = {0}; \nnº2 = {1}; \nnº3 = {2}; '.format (num1, num2, num3)))

if num1<num2 and num1<num3 and num2<num3:
    print(f'{num3} é o maior nº e {num1} o menor nº')

if num1 < num2 and num1 < num3 and num3 < num2:
    print(f'{num2} é o maior nº e {num1} o menor nº')

if num2<num1 and num2<num3 and num1<num3:
    print(f'{num3} é o maior nº e {num2} o menor nº')

if num2 < num1 and num2 < num3 and num3 < num1:
    print(f'{num1} é o maior nº e {num2} o menor nº')

if num3 < num1 and num3 < num2 and num2 < num1:
    print(f'{num2} é o maior nº e {num3} o menor nº')

if num3 < num1 and num3 < num2 and num1 < num2:
    print(f'{num1} é o maior nº e {num3} o menor nº')

else:
    print('Existem valores iguais, a ordenação não é possivel')


