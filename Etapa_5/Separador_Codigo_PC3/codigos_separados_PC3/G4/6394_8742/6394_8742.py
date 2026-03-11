from numpy import*
vet = array(eval(input("valores: ")))
cod = zeros(size(vet), dtype=int)
for i in range(size(vet)):
	if vet[i] != 9:
		cod[i] = vet[i]+1 
print(cod) 
	

	
	