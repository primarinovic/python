from datetime import date

gen = str(input('''Informe o gênero [F] ou [M]:''')).strip().upper()

dataNasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - dataNasc

print(f'Quem nasceu em {dataNasc} tem {idade} anos em {atual}.')

if gen == 'M' and idade == 18:
    print('Você tem que se alistar imediatamente!')
elif gen == 'M' and idade < 18:
    daquiQtsAnos = 18 - idade
    print(f'Ainda falta {daquiQtsAnos} anos para seu alistamento')
    print(f'Seu alistamento será em {atual + daquiQtsAnos}.')
elif gen == 'M' and idade > 18:
    haQtsAnos = idade - 18
    print(f'Você já deveria ter se alistado há {haQtsAnos} anos!')
    print(f'Seu alistamento foi em {atual - haQtsAnos}.')
elif gen == 'F':
    print('O serviço militar não é obrigatório para mulheres.')
