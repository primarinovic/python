from math import hypot
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))

print(f'O comprimento da hipotenusa desse triângulo retângulo é {hypot(co, ca):.2f}cm.')
