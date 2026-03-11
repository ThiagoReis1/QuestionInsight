# Peso da mercadoria (Kg)
peso = float(input("Insira o peso da mercadoria: " ) )

# Variáveis
kg = 43.21
taxa = 25.00

# Cálculo do valor total do frete
total1 = kg * peso + taxa
total2 = total1 / 100 * 62
ValorTotal = total1 + total2

print(round(ValorTotal ,2) )