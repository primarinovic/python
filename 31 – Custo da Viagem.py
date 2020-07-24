distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    print(f'Para a distância de {distancia}km o valor é de R${distancia * 0.50:.2f}.')
else:
    print(f'Para a distância de {distancia}km o valor é de R${distancia * 0.45:.2f}.')

