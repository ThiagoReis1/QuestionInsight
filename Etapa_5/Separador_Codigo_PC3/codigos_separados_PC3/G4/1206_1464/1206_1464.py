from numpy import*
v=array(eval(input("v:")))
i=0
soma=0
recorde=8.95
while(i<size(v)):
	if(v[i]<8.95):
		soma=soma+1
	i=i+1
print(recorde)
print(soma)