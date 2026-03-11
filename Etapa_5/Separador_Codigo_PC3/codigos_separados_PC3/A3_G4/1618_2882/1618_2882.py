from numpy import*

c=array(eval(input("Coeficientes: ")))

#x=size(c)
#ini=c[0]
#fim=ini+2

i=0
saida=" "
eq=0
while(i<(size(c))):
	if(c[i]>0):
		eq=str(c[i])+'x^ '+(str())
		saida=saida+eq+(str(i))
	i=i+1

print(saida)


	
