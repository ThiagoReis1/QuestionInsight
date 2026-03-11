from numpy import*
v=array(eval(input("Chegada")))
i=0
while(i<size(v)):
	if(v[i]==min(v)):
		print(i)
	i=i+1