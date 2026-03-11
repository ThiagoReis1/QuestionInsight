from numpy import*
numb=array(eval(input()))
i=0
j=0
maior=99
while(i<size(numb)):
	if(numb[i]<maior):
		maior=numb[i]
		j=i
	i=i+1
print(j)