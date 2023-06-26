    # Sequencia de Fibonacci

print('_'*50)
fibonacci = int(input('Insira quantos termos você quer visualizar: '))
t1 = 0
t2 = 1

cont = 3

print(f'{t1} >>> ', end='')
while cont <= fibonacci:
    t3 = t1 + t2
    print(f'{t3} >>> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
