quant=float(input("Digite kWh consumidos: "))

total=quant*0.43+10.0
aument= (25/100)*total
total1= total+aument

print(round(total1,2))