distancia=input("K/M ")

if (distancia=="K"):
	K=float(input("digite"))
	M=K/1.60934
	print(round(M,2))
else:
	M=float(input("digite"))
	K=1.60934*M
	print(round(K,2))
	
	
	
	