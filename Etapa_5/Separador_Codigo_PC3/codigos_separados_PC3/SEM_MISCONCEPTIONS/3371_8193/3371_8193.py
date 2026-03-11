unidade = input("unidade:").upper()
valor = float(input("valor:"))
if (unidade=="K"):
	valor1= valor/1.60934
else:
	valor1=valor*1.60934
	
print(round(valor1,2))

