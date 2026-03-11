from numpy import*
x = array(eval(input("numeros dos aneis: ")))
i = 0
j = 200
while i<size(x):
	if(x[i]==1):
		j= j*4
	elif(x[i]==2):
		j= j*2
	elif(x[i]==3):
		j=j 
	elif(x[i]==4):
		j=(j/2)
	i=i+1
print(j)