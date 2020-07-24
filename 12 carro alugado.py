km = float(input('Informe quantos km percorridos: '))
dias = float(input('Informe quantos dias de aluguel: '))
valorTotal = (dias * 60) + (km * 0.15)

print(f'O valor total é de R${valorTotal:.2f}')