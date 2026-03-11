#Soraiadite

gaso = float(input("Quantos litros de gasolina foram abastecidos?"))

conta = gaso * 2.86

oleo = 50.00

icms = 34 / 100

total = (conta + oleo) +  (conta + oleo) * icms

print(round(total, 2))
