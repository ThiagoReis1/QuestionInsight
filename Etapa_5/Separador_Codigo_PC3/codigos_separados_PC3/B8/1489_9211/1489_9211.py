consumo = float(input("consumo de energia"))
if consumo >0 and consumo <150:
	valor = consumo * 0.60 + 5
elif consumo >150 and consumo <250:
	valor = consumo * 0.65 + 8
elif consumo >250 and consumo <350:
	valor = consumo * 0.70 + 12
elif consumo >350:
	valor = consumo * 0.75 + 16
	
print(valor)