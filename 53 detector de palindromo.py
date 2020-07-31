frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverter = ''
# é possível fazer sem o for com inverter = juntar[::-1]
for letras in range(len(juntar) - 1, -1, -1):
    inverter += juntar[letras]
print(f'A frase {juntar} ao contrário fica {inverter}.')
if inverter == juntar:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
