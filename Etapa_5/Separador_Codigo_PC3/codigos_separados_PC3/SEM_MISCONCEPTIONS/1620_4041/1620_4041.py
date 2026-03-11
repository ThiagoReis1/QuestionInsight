from numpy import*
from numpy.linalg import*

tempo = array(eval(input("insira os tempos de banho durante a semana: ")))
perc = array(eval(input("insira o percentual dos tempo de banho na semana: ")))

#consumo = zeros(size(tempo),dtype=int)
consumo = 0
for i in range(size(perc)):
		consumo = consumo + (perc[i]/100)*5*(tempo[i])

print(round(consumo,2))
	
