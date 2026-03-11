from numpy import*

n = array(eval(input(": ")))

saida = zeros((n,n),dtype=int)

for i in range(n):
	for j in range(n):
		if i == j:
			saida[i,j] = 1
			
		elif i > j:
			saida[i,j] = 0
			
		else:
			saida[i,j] = 1
			
print(saida)