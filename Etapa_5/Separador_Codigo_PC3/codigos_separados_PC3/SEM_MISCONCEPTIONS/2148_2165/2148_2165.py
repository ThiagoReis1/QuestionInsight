from numpy import*
medida = array(eval(input()))

soma = 0
j = 0
for x in range(size(medida)):
	soma = soma + medida[x]
	
	if(medida[x] >= 5):
		j = j + 1
		
print(soma)
print(j)
