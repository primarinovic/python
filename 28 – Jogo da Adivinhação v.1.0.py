from random import randrange
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
sorteado = randrange(5) # Faz o computador "pensar" <-> sortear.
num = int(input('Em que número que pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if num == sorteado:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {sorteado} e não no {num}!')
