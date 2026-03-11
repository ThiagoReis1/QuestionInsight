un = input(" unidade em que a medida esta: K para quilometro, ou M para milha: ")
valor = (input(" valor da medida: ")
K = round(1.60934*valor, 2)
M = round(valor/1.60934, 2)
if un == K:
	print(K)
	
else:
	print(M)
