n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro:'))

# ordem de precedencia
# tudo que estiver entre () depois,
pot = n1 ** n2 # potencia
mult = n1 * n2
div = n1 / n2
divint = n1 // n2 # divisão que só retorna o inteiro, ou seja, sem casas decimais
restomod = n1 % n2
soma = n1 + n2
sub = n1 - n2

print('Potência de {} ** {} = {}'.format(n1, n2, pot))
print('Multiplicação de {} * {} = {}'.format(n1, n2, mult))
print('Divisão de {} / {} = {:.3f}'.format(n1, n2, div))
print('Divisão inteira de {} // {} = {}'.format(n1, n2, divint))
print('Resto da divisão de {} % {} = {}'.format(n1, n2, restomod))
print('Soma de {} + {} = {}'.format(n1, n2, soma))
print('Subtração de {} - {} = {}'.format(n1, n2, sub))

