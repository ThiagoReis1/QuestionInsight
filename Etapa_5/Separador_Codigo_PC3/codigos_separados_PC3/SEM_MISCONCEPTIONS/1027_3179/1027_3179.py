#CONTA DE ENERGIA
#energia = (0.43 * kWh) + 10.00
#TAXA
#taxa = energia * 0.25

#Consumo
kwh = float(input("Digite quantos kWh consumidos:"))

energia = float(kwh * 0.43) + 10

taxa = float(energia * 0.25 + energia)

#Valor total
print(round(taxa,2))