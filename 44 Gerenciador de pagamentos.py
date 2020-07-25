valorOriginal = float(input('Valor total das compras: R$'))

opcaoPagto = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (com juros de 20%)
Indique a forma de pagamento escolhida: '''))

print(f'Subtotal: R${valorOriginal:.2f}')

if opcaoPagto == 1:
    desconto = valorOriginal - ((valorOriginal * 10) / 100)
    print(f'Total: R${desconto:.2f}')
elif opcaoPagto == 2:
    desconto = valorOriginal - ((valorOriginal * 5) / 100)
    print(f'Total: R${desconto:.2f}')
elif opcaoPagto == 3:
    parcelamento = valorOriginal / 2
    print(f'Total: R${valorOriginal} em 2x de R${parcelamento:.2f}')
elif opcaoPagto == 4:
    parcelas = int(input('Informe em quantas parcelas: '))
    juros = (valorOriginal * 20) / 100
    novoValor = valorOriginal + juros
    totalParcelado = novoValor / parcelas
    print(f'Total: R${novoValor} em {parcelas}x de R${totalParcelado:.2f}')
else:
    print('Opção inválida.')
