    #
peso = float(input('Insira o seu peso (em KG): '))
altura = float(input('Insira a sua altura (em metros): '))

IMC = peso/(altura**2)

print(f'O IMC dessa pessoa equivale a {IMC:.1f}')

if IMC < 18.5:
    print('Peso abaixo do normal. Neste caso, é necessária a busca por um especialista, para verificar a existência de algum problema de saúde causador do índice abaixo do normal, ou analisar se sua saúde não está sendo afetada.')

elif IMC >= 18.5 and IMC <= 24.9:
    print('São pesos considerados normais pela OMS. No entanto, mesmo nesta faixa de peso, deve-se ter atenção e cuidado com possíveis problemas metabólicos, principalmente se houver acúmulo de gordura na região interna do abdômen.')

elif IMC >= 25 and IMC <= 29.9:
    print('Peso em pré-obesidade ou acima do peso, representando um risco maior para a saúde. Nesta causa,  é imprescindível uma consulta com um especialista, pois pode estar relacionado à pressão alta, colesterol alto ou diabetes, podendo apontar até para o hipotireoidismo.  Este é o seu índice? Se sim, é tempo de consultar um  profissional, realizar exames e pensar em uma reeducação alimentar e exercícios físicos.')

elif IMC >= 30 and IMC <= 34.9:
    print('Este índice indica obesidade grau um. Este peso aumenta riscos para várias doenças, como diabetes, hipertensão arterial, o infarto do miocárdio e diversos tipos de câncer. A obesidade já é considerada uma comorbidade e necessita de tratamento profissional. O indicado é consultar um especialista e receber acompanhamento adequado.')

elif IMC >= 35 and IMC <= 39.9:
    print('Indica obesidade grau dois. Este peso já representa risco elevado para as doenças supracitadas. Como em todos os casos, mas neste impreterivelmente, deve-se buscar um profissional especializado e receber as orientações e medidas adequadas para obter uma saúde equilibrada.')

else:
    print('Indica obesidade grau três ou mórbida. O peso neste grau apresenta problemas extremamente graves e necessita de tratamento profissional com o máximo de recursos disponíveis, incluindo até cirurgia.')
