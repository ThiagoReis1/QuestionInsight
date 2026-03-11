#valor reais
valor = float(input(""))
if(valor>0 and valor<=1000.0):
	vol = valor + 0.05*valor
	print(float(round(vol,2)))
else:
	vol = 0.05*(valor/2) + 0.1*(valor/2)
	print(float(round(vol,2)))
