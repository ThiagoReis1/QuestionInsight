from numpy import*

vet = array(eval(input("Entre com o vetor da mensagem: ")))

cont = zeros(size(vet), dtype=int)
j = 0
for x in vet:
	
	if x == 9:
		cont[j] = 0
	else: 
		cont[j] = (x + 1)**2
	j = j + 1
	
print(cont)
	

