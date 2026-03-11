from numpy import*
V1 = array(eval(input("escreva o vetor ")))
lancamento = 74.08
i = 0
count = 0
while( i < size(V1)):
	if(V1[1] <= lancamento):
	   count = V1[i] + 1
	i = i + 1
else:
	print(lancamento)
i=0
count=0
while(i<size(V1)):
	if(V1[i] > lancamento):
		count= count + 1
	i = i + 1
print(count) 

	