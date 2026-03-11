from numpy import*
a = array(eval(input(": ")))
cont=0
i=1
while(i<size(a)):
	if(a[0]<=a[i]):
		print(i)
		cont = cont+1
	i=i+1	
print(cont)