kwh = float(input("Digite o valor: "))
energia = 0.43 
fixo = 10.00
cobrado = 25/100

luz = (energia * kwh + fixo) * cobrado
total = (energia * kwh + fixo) + luz

print(round(total,2))