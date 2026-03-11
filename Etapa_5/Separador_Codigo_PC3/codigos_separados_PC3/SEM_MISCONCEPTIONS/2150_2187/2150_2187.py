from numpy import *

entrada = array(eval(input("Entrada: ")))

TIMES = ["BOTAFOGO","FLAMENGO","FLUMINENSE","VASCO"]

saida = zeros(size(TIMES), dtype = int)


for i in range(size(TIMES)):
	for j in range(size(entrada)):
		if(entrada[j] == TIMES[i]):
			saida[i] = saida[i] + 1
	
print(saida)