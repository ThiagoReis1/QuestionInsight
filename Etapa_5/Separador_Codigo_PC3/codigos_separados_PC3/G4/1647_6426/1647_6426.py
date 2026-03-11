from numpy import*

ap=array(eval(input("entre ")))

cont=0
for i in range(size(ap)):
	if(ap[i]>=70):
	   cont+=1

porc=zeros(cont,dtype=int)
j=0
for i in range(size(ap)):
	if(ap[i]>=70):
		porc[j]=i
		j=j+1
		
print(j)
print(porc)
		
	   