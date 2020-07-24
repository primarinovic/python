a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b > c and a > c:
    print(f'O maior valor foi: {a}')
    print(f'O menor valor foi: {c}')
if b < a < c and b < c:
    print(f'O maior valor foi: {c}')
    print(f'O menor valor foi: {b}')
if a < b and a < c < b:
    print(f'O maior valor foi: {b}')
    print(f'O menor valor foi: {a}')
