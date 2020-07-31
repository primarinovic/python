from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade e {menor} pessoas ainda não.')
