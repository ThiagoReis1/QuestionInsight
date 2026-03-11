med = input().upper()
valor = float(input())

if (med == "K"):
	M = 2.35215*valor
	print(round(M, 2))
	
else:
	K = valor/2.35215
	print(round(K, 2))