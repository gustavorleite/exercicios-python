    #

p_valor = float(input('Insira o primeiro valor: '))
s_valor = float(input('Insira o segundo valor: '))

print('\nDigite:\n [1] SOMAR (+) OS VALORES\n [2] MULTIPLICAR (*) OS VALORES\n [3] DIVIDIR (/) OS VALORES \n [4] DESCOBRIR QUAL O MAIOR (>) ENTRE OS VALORES')

opcao = int(input('Selecione sua opção na lista: '))
fim = False
while fim == False:
    if opcao == 1:
        soma = p_valor + s_valor
        print(f'Resultado = {soma}')
        fim = True
    elif opcao == 2:
        multiplicacao = p_valor * s_valor
        print(f'Resultado = {multiplicacao}')
        fim = True
    elif opcao == 3:
        divisao = p_valor / s_valor
        print(f'Resultado = {divisao}')
        fim = True
    elif opcao == 4:
        maior = max(p_valor, s_valor)
        print(maior)
        fim = True
    else:
        fim = True
        print('Opção Invalida, tente novamente')
