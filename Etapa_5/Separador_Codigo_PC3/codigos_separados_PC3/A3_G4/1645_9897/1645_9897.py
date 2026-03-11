from numpy import * 

saques = array(eval(input('')))
acum = zeros(size(saques), dtype=int)#numeros inteiros
#saques efetuados acima do limite
n = 0
for i in range(size(saques)):
	if saques[i] >= 2000:
		n += 1
print(n)

ind = 0 #indices
vet = zeros(n)
for i in range(size(saques)):
	if saques[i] >= 2000:
		acum[ind] = i
		ind += 1
print(ind) 
	
