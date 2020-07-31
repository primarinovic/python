soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma dos {cont} números ímpares que são múltiplos de três entre 1 e 500 é: {soma}')
