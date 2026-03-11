from numpy import*

vet = str(input("Digite os paises: ")).split(',')

new = ""
soma = zeros(5, dtype = int)

for i in range(size(vet)) :
	
	if vet[i] == "BE" :
		
		soma[0] = soma[0] + 1
		
	elif vet[i] == "ES" :
		
		soma[1] = soma[1] + 1
		
	elif vet[i] == "FR" :
		
		soma[2] = soma[2] + 1 
		
	elif vet[i] == "IT" :
		
		soma[3] = soma[3] + 1
		
	else :
		soma[4] = soma[4] + 1
		
print(max(soma))
print(soma)