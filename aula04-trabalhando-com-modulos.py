# Adicionando novos recursos/bibliotecas a linguagem para obter novas funcionalidades
import math # vai importar tudo o que tem em math
#from math import sqrt, floor # vai importar somente estes elementos

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) 
