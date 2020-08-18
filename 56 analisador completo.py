soma = 0
media = 0
qtdadeMulher = 0
homemMaisVelho = 0
nomeMaisVelho = ''
for c in range(1, 5):
    print(f'== {c}ª pessoa ==')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M]ou[F]: ')).strip().upper()
    soma += idade
    media = (soma / 4)
    if c == 1 and sexo == 'M':
        homemMaisVelho = idade
        nomeMaisVelho = nome
    if sexo == 'M' and idade > homemMaisVelho:
        homemMaisVelho = idade
        nomeMaisVelho = nome
    if sexo == 'F' and idade < 20:
        qtdadeMulher += 1
print(f'A média de idade do grupo é de {media:.1f} anos')
print(f'O homem mais velho do grupo tem {homemMaisVelho} anos e se chama {nomeMaisVelho}.')
print(f'Ao todo são {qtdadeMulher} mulheres com menos de 20 anos.')
