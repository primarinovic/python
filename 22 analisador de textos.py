nome = str(input('Informe o nome completo: ')).strip()

print(f'Seu nome em maiúsculo: {nome.upper()}.')
print(f'Seu nome em minúsculo: {nome.lower()}.')

semEspaco = len(nome) - nome.count(' ')

print('Seu nome tem ', semEspaco, 'letras.')

separado = nome.split()

print('Seu primeiro nome tem ', separado[0], 'letras.')
