from numpy import*
tcc = array(eval(input("tempo de chegada dos corredores:")))
i=0

while(i<size(tcc)):
	if(tcc[i]!=min(tcc)):
		i=i+1
	else:
		print(i)