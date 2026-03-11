consumo= int(input("consumo: "))

if(consumo<=150):
	imp= (consumo*(0.6))+5
else:
	imp= (consumo*(0.75))+16

print(round(imp, 2))