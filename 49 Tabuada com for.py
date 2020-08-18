num = int(input('Informe o número para ver a tabuada: '))
print('*-*' * 20)
print(f'Tabuada do {num}:')
for c in range(0, 11):
    print(f'{num} x {c:2} = {num * c}')
print('*-*' * 20)
