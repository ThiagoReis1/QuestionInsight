a = input("insira a unidade de medida = ")
b = float(input("valor da velocidade = "))

vkm = 3.6 * b
vms = b / 3.6

if (a.upper() == "M"):
	print(round(vkm,2))
	
if (a.upper() == "K"):
	print(round(vms, 2))