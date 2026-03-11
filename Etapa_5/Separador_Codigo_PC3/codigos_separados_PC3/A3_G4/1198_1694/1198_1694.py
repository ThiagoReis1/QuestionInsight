from numpy import*

temp=array(eval(input("Temperatura da agua:")))
saida=array(zeros(size(temp),dtype=int))
i=0
c=0
while i<size(temp):
	j=0
	while j<size(saida):
		if temp[i]<10:
			saida[j]=temp[i]
			j=j+1
	i=i+1
print (saida)


