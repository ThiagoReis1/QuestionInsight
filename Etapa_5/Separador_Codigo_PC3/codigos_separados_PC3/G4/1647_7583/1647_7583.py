from numpy import*

vetor = array(eval(input("blabla: ")))

j= 0

for i in range(size(vetor)):
	if(vetor[i] >= 70):
		j = j + 1
print(j) 

cont = zeros(j, dtype = int)

l = 0 

for k in range(size(vetor)):
	if(vetor[k] >= 70):
		
		cont[l]=k
		k = k +1
		l = l +1
		
print(cont)
	

		
	
	

