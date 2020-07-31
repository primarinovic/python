print('10 termos de uma PA')
print('*-*' * 7)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = termo + (10 - 1) * razao
for c in range(termo, dec + razao, razao):
    print(f'{c}', end=' -> ')
print('FIM')


