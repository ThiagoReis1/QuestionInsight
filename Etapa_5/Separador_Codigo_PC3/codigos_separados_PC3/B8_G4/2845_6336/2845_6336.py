from numpy import*

ent = eval(input("digite a senha"))
vet = zeros(size(ent), dtype = int)
j = 0

for i in range(size(ent)):
	if ent[i] != 9:
		vet[j] = ent[i] + 1 
		j = j + 1
		
	elif ent[i] == 9:
		vet[j] = 0
			
		
			
					  
print(vet)
		
					  