from numpy import*

	
# concatenar

vetor = array(eval(input()))
a = ""
i = 0 

#vetor expoente
tam = size(vetor)-1
vetorp = arange(tam)
vetorc1 = zeros(tam, dtype=int)
ind =0
i1 = -1

while(ind < size(vetorp)):
	vetorc1[i1] = vetorp[ind] 
	i1 = i1 - 1
	ind = ind + 1
	
	
#------------------------


while ( i < size(vetor)):
	a = a + str(vetor[i]) + str(vetorc1[i])
	i = i + 1	
	
print(a)


