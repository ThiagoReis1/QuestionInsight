from numpy import*
competidores=array(eval(input("")))
i=0
indice=0
Menor=competidores[0]
while(i < size(competidores)):
	if(competidores[i] < Menor):
		Menor=competidores[i]
		indice=i
	i=i+1
print(indice)
		