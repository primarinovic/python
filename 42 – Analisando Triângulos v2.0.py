print('-=-' * 20)
print('Analisando um Triângulo')
print('-=-' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Os segmentos acima \033[1;34mPODEM\033[m formar um triângulo ', end='')

    if r1 == r2 == r3:
        print('\033[1;33mEQUILÁTERO\033[m.')
    elif r1 == r2 or r1 == r3:
        print('\033[1;32mISÓSCELES\033[m.')
    else:
        print('\033[1;35mESCALENO\033[m.')

else:
    print('Os segmentos acima \033[1;31mNÃO\033[m formam um triângulo.')
