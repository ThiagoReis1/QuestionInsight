med = input("Qual a Unidade de Medida: ")
dis = float(input("qual a distancia: "))

med.upper()
if (med == "K"):
	K = dis/1.60934 
	print(round(K, 2))
else:
	K = 1.60934 * dis
	print(round(K, 2))