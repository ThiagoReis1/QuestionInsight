from numpy import*
cont=zeros(2,dtype(int))
v=array(eval(input("Digite o vetor: ")))
#menor valor
a= min(v)
#maior valor
b= max(v)
#
c= (6/10)*a+(4/10)*b
d= (3/10)*a+(7/10)*b
i= 0
for i in range(size(v)):
	if (v[i] >= c and v[i]<d):
		cont[0]= cont[0]+1 	
	elif (v[i] >= d and v[i]<b):
		cont[1] = cont[1]+1
print(cont)
		
		
		