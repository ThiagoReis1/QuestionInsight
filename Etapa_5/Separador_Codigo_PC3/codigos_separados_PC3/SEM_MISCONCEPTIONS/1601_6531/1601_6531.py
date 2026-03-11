from numpy import*
tempo = array(eval(input("Tempo de chegada: ")))

i = 0

while(i < size(tempo)):
	if(tempo[i] == min(tempo)):
		print(i)
	i = i + 1