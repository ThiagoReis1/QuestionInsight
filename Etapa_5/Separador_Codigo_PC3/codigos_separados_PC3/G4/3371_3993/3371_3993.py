u = input("Unidade de medida K/M: ")
if(u == "K"):
	k = float(input("Valor em km: "))
	mi = k/1.60934
	print(round(mi,2))
else:
	mi = float(input("Valor em milhas: "))
	k = 1.60934*mi
	print(round(k,2))