genero = str(input('Informe seu gênero [M/F/NB]\n*Masculino *Feminino *Não-Binário: ')).strip().upper()

while genero not in 'M' 'F' 'NB':
    genero = str(input('Erro, informe *Masculino *Feminino *Não-Binário: ')).strip().upper()

print('Registrado com sucesso.')

