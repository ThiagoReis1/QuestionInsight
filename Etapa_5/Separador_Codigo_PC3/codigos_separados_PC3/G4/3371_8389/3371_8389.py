unid = input("unidade de medida: (K/M):")
var = float(input("valor da medida: "))

if(unid=="K"):
	M = var/1.60934
	print(round(M, 2))
	
else:
	K = 1.60934*var
	print(round(K, 2))