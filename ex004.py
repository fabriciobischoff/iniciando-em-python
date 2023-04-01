print('==== DESAFIO 005 ====')
element = input('Digite algo:')
print(type(element))
print('É numérico? ', element.isnumeric())  # verifica se é numérico
print('É uma letra? ', element.isalpha())  # verifica se é alfabetico
print('É alfanumperico? ', element.isalnum())  # verifica se é alfanumerico
# verifica se é letra minuscula
print('É letra minúscula? ', element.islower())
# verifica se é letra maiúscula
print('É letra maiúscula? ', element.isupper())
