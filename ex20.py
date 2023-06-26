import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacante: '))
hip = math.hypot(co, ca)
print(' A medida da hipotenusa é: {:.2f}'.format(hip))
