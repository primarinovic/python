velAtual = float(input('Qual a velocidade atual do carro? '))
if velAtual > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h!')
    multa = (velAtual - 80) * 7
    print(f'Você deve pagar uma multa que é de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
