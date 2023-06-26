    #
a = float(input('Nota da 1ª Prova: '))
b = float(input('Nota da 2ª Prova: '))

media =(a+b)/2
c = media >= 6.0
d = media > 3.0 < 6.0
e = media <= 3.0

if c:
   print(f'Sua média é {media}, você foi APROVADO' )

elif d:
    print(f'Sua média foi {media}. Você está em RECUPERAÇÃO')

else:
    print(f'Infelizmente, sua média foi de {media}. Você foi REPROVADO')