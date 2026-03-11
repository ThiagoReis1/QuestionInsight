from numpy import*
tempo=array(eval(input()))
i=0
while (i< size(tempo)):
	if(tempo[i] == min(tempo)):
		teste = i
		i+=1
	else:
		i=i+1
print(teste)