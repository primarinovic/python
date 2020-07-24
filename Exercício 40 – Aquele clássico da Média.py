n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Média: {media:.1f}. Aluno APROVADO!')
elif 5 <= media < 7:
    print(f'Média: {media:.1f}. Aluno de RECUPERAÇÃO.')
elif media < 5:
    print(f'Média: {media:.1f}. Aluno REPROVADO.')
