from numpy import*
v = array(eval(input("tempo de chegada: ")))
i=0

while(i<size(v)):
	if(v[i]==min(v)):
		print(i)
		i=size(v)+1
	else:
		i=i+1

