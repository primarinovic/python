frase = str(input('Escreva uma frase: ')).strip() .upper()

print(f"A letra A aparece {frase.count('A')}x na frase.")
print(f"A letra A aparece na frase pela primeira vez na posição {frase.find('A')}.")
print(f"E aparece pela última vez na posição {frase.rfind('A')}.")
