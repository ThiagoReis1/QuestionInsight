from numpy import*
x = array(eval(input("Vetor: ")))
zero = 0 
n = 0

for i in range(size(x)): 
	if(i==0):
		zero = zero + 1
	else:
		n = n + 1
		
vet = zeros(zero, dtype=int)

for i in x:
	if(i==0):
	vet = i 
	
print(vet+vetze)