from numpy import*

tempo_corrida = array(eval(input("informe o tempo de corrida: ")))
i = 0

while (i < size(tempo_corrida)):
	if (tempo_corrida[i] == min(tempo_corrida)): 
		ganhador = i
		
	i = i+1
	
print(ganhador)


