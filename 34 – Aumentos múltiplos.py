sal = float(input('Informe o salário do funcionário: R$'))

if sal <= 1250:
    aumento = (sal * 15) / 100
else:
    aumento = (sal * 10) / 100

print(f'Quem ganhava \033[1;31mR${sal:.2f}\033[m recebe um aumento de \033[4;33mR${aumento:.2f}\033[m e '
      f'passa a ganhar \033[1;32mR${aumento + sal:.2f}\033[m agora.')
