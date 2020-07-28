from time import sleep
from random import randint
jogador = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual a sua jogada? '''))
escolha = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('-=' * 15)
print(f'Computador jogou {escolha[computador]}')
print(f'Jogador jogou {escolha[jogador]}')
print('-=' * 15)

if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('Jogador PERDEU')
    elif computador == 2:
        print('Jogador VENCEU')
    else:
        print('Escolha inválida')
elif jogador == 1:
    if computador == 0:
        print('Jogador VENCEU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('Jogador PERDEU')
    else:
        print('Escolha inválida')
elif jogador == 2:
    if computador == 0:
        print('Jogador PERDEU')
    elif computador == 1:
        print('Jogador VENCEU')
    elif computador == 2:
        print('EMPATE')
    else:
        print('Escolha inválida')
