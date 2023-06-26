    # PALINDROMO

palindromo = str(input('INSIRA SUA FRASE/NOME: ')).strip().upper()
palavras = palindromo.split()
junto = ''.join(palavras)
inverso = ''
print(f'{junto}')
for letra in range(len(junto) -1, -1, -1):
    print(junto[letra], end='')
    if (junto[letra]) == palindromo:
        print('É um palindromo!!')
