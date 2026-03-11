from numpy import*
a = array(eval(input(" ")))
i = 0
soma = 100
while(i < size(a)):
	if(a[i]==1):
		soma = soma*5
	elif(a[i]==2):
		soma =soma*3
	elif(a[i]==3):
		soma = soma 
	elif(a[i]==4):
		soma = soma/2
	i = i+1
print(round(soma,2))
		
