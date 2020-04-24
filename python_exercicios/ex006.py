# Dobro, Triplo e Raiz Quadrada

import math

number = int(input('Digite um número: '))
double = number * 2
triple = number * 3
square_root = math.sqrt(number)

print('O dobro de {} vale {}'.format(number, double))
print('O triplo de {} vale {}'.format(number, triple))
print('A raiz quadrada de %s é igual a %.2f' % (number, square_root))