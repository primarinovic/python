from math import sin, cos, tan, radians

angulo = float(input('Informe o ângulo: '))

print(f'O seno de {angulo}° é {sin(radians(angulo)):.2f}. \nO cosseno de {angulo}° é {cos(radians(angulo)):.2f}.')
print(f'A tangente de {angulo}° é {tan(radians(angulo)):.2f}.')
