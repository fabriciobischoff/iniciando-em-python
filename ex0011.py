print('==== DESAFIO 0011 ====')
largura = float(input('Informe a largura da parede em m²: '))
altura = float(input('Informe a altura da parede em m²: '))

area = largura * altura

# Considerando que cada litro de tinta, pinta uma área de 2m²
quantTinta = area / 2

print('Quantidade de tinta para pintar {} m² é de {} Litros'.format(area, quantTinta))