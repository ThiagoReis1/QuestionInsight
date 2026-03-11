# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo
# Curso: Estatistica

# Cada kg custa 43,21 + taxa de 25,00 

# Inputs ( Peso da mercadoria em kg )
peso_mercadoria = float(input('Digite o peso da mercadoria (em kg): '))

# Calcular valor total
valor_total = (peso_mercadoria * 43.21) + 25.00
valor_icms = ((valor_total /100) * (62/100) * 100)

valor_final = valor_icms + valor_total


# Output ( valor total a ser pago )
print(round(valor_final, 2))