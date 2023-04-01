print('==== DESAFIO 0010 ====')
valorReais = float(input('Digite uma quantia em R$: '))

# Considerando que US$ 1,00 = R$ 3,27
print('Com R$ {:.2f} você poderá comprar US$ {:.3f} dólares.'.format(valorReais, valorReais / 3.27))