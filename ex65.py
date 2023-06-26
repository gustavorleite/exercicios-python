n = 0
c = 0
qtd_num = 0
media = 0

continuar = 's'.upper().strip()

while continuar in 's'.upper().strip():
    n = int(input('Digite um nº: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    c += n
    qtd_num += 1

    if continuar == 'n':
        break

media = c/qtd_num

print(f'Você digitou {qtd_num} números.\nA média entre eles é de {media}.')
      # f'\n O maior valor dentre os indicados foi {max(lst)} e o menor valor foi {min(lst)}. ')
