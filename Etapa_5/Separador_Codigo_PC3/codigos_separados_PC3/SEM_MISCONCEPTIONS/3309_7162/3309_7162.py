# Peso da mercadoria
peso = float(input("Qual o peso da mercadoria a ser transportada?"))

# Cálculo do frete
frete = peso*43.21 + 25
imposto = frete*0.62
total = frete + imposto

#Saída
print(round(total,2))