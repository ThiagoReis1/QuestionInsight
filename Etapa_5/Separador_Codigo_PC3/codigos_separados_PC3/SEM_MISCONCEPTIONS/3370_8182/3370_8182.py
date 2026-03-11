undm = input("Escreva C/P para conversao: ")
medida = float(input("valor das medidas: "))

if (undm.upper() == "P"):
	r = medida / 0.393701
	
else:
	r = medida * 0.393701
	
print(round(r,2))