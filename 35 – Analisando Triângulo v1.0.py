print('-=-' * 20)
print('Analisador de Triângulo')
print('-=-' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Os segmentos acima \033[1;34mPODEM\033[m formar um triângulo!')
else:
    print('Os segmentos acima \033[1;31mNÃO\033[m formam um triângulo.')
