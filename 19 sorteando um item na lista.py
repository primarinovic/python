from random import choice
aluno1 = str(input('Informe o primeiro aluno: '))
aluno2 = str(input('Informe o segundo aluno: '))
aluno3 = str(input('Informe o terceiro aluno: '))
aluno4 = str(input('Informe o quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)

print(f'O aluno sorteado foi: {sorteado}.')
