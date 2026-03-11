#entradas 

qtd = float(input("quantidade de kWh: "))

conta = ( 0.43 * qtd ) + 10 

total = (conta * 25/100) + conta

print(round(total, 2))