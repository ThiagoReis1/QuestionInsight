from numpy import*

metas = array(eval(input(": ")))
x =size(metas)
i=1
aux=0

while i < x:
	if(metas[i]>=metas[0]):
		print(i)
		aux=aux+1
	i=i+1
	
print(aux)
		
		
		
		
	