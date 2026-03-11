from numpy import*
vet = array(eval(input("vetor: ")))

i = 0 
p = 200 

while i <size(vet):
	if vet[i] == 1:
		p = p/2
	if vet[i] == 2:
		p = p*3
	if vet[i] == 3: 
		p = p/2
	if vet[i] == 4:
		p = p*3
	if vet[i] == 5:
		p = p/2
	if vet[i] == 6:
		p = p*3
	i = i + 1
print(p)
		
	

