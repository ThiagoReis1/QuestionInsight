from numpy import*
cheg = (array(eval(input("a"))))
tam = size(cheg)
j=0
i=0
ma = min(cheg)

#ind=tam-1
while(i<tam):
	if(cheg[i]==ma):
		j=i
	i=i+1
print(j)
		
	
