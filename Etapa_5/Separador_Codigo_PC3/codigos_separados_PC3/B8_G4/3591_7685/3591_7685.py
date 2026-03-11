from numpy import*
n= array(eval(input("")))
i=0
soma=0

while(size(n)>i):
	if(n[i]==1 or n[i]==3 or n[i]==5):
		soma=soma+10
	elif(n[i]==2 or n[i]==4 or n[i]==6):
		soma=soma+5
	i=i+1
print(soma)