altura = float(input('Altura: (m) '))
peso = float(input('Peso: (kg) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc:.1f} é considerado ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.1f} é considerado PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.1f} é considerado SOBREPESO.')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.1f} é considerado OBESIDADE.')
else:
    print(f'IMC: {imc:.1f} é considerado OBESIDADE MÓRBIDA.')
