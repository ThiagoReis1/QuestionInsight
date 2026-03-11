# Victor Lopes Aguiar - 21551604

# 16/06/2016

# Avaliacao 01

consumo = (float(input("Consumo do mes em kWh: ")))

valor_consumo = consumo*0.43 +10

valor_imposto = valor_consumo*25/100

total = valor_consumo + valor_imposto

print (round(total,2))