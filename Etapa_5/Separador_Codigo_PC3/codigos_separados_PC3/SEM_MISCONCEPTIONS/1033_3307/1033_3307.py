# Peso da mercadoria 
peso = float(input('Peso da mercadoria: '))

# Custo do frete
frete = (peso * 43.21) + 25.00 
imposto = frete * (62/100)
total = frete + imposto

print(round(total, 2))