from datetime import date
anoNasc = int(input('Ano de nascimento: '))
idade = date.today().year - anoNasc

if idade <= 9:
    print(f'Um atleta de {idade} anos é considerado MIRIM.')
elif idade <= 14:
    print(f'Um atleta de {idade} anos é considerado INFANTIL.')
elif idade <= 19:
    print(f'Um atleta de {idade} anos é considerado JÚNIOR.')
elif idade <= 25:
    print(f'Um atleta de {idade} anos é considerado SÊNIOR.')
else:
    print(f'Um atleta de {idade} anos é considerado MASTER.')
