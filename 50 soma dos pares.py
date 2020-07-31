soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Informe {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Foram informados {cont} números pares e a soma deles é igual a {soma}.')
