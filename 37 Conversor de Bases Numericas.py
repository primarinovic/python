n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'O número {n} em binário é {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} em octal é {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} em hexadecimal é {hex(n)[2:]}')
else:
    print('Opção INVÁLIDA. Tente novamente.')
