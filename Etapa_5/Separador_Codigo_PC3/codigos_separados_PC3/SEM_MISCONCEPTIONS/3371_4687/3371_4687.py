unidade_medida = input()
valor_medida = float(input())

if	(unidade_medida.upper() == "K"):
	A = valor_medida/1.60934
else:
	A = valor_medida*1.60934
	
print(round(A, 2))