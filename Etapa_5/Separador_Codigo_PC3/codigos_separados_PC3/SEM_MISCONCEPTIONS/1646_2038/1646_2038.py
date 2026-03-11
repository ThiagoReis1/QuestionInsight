from numpy import*
 
saque = array(eval(input("quantos saques: ")))

cont = 0

for i in range(size(saque)):
	if(saque[i] <= 50):
		cont = cont + 1

x = 0

vetor = zeros(cont, dtype=int)

for i in range(size(saque)):
	if(saque[i] <= 50):
		vetor[x] = i
		x = x + 1
	
print(cont)
print(vetor)	 
				 

	
	
	


