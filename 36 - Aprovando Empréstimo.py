valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe a renda do comprador: R$'))
qtosAnos = int(input('Informe em quantos anos quitará a casa: '))
prestacao = valorCasa / (qtosAnos * 12)

if prestacao <= (salario * 30)/100:
    print(f'Uma casa de valor R${valorCasa:.2f} para se pagar em {qtosAnos} anos '
          f'tem uma prestação de R${prestacao:.2f}. Empréstimo aprovado.')
else:
    print(f'A prestação de R${prestacao:.2f} excede 30% do salário. Empréstimo negado.')
