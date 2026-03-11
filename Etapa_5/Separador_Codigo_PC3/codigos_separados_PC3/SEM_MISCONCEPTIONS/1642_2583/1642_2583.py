from numpy import*
vet1 = array(eval(input()))
q = 0
i = 0
c = 0
for(i<size(vet1)):
	if(vet1[i]%5==0):
		q = q + 1
	i = i +1
vet2=zeros(q)
i = 0
for(i<size(vet1)):
	if(vet1[i]%5==0):
		vet2[c] = int(c)
		c = c+1
	i = i + 1
	
print(q)
print(array(vet2)
		
