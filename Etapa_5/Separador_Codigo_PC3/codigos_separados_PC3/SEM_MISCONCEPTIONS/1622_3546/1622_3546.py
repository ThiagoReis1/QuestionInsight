from numpy import *

entrada = array(eval(input()), dtype=int)
saida = array(eval(input()), dtype=int)

onibus = zeros(4, dtype=int)
i = 0
while(i < len(entrada)):
	onibus[i] = entrada[i] - saida[i]
	i += 1
	
print(sum(onibus))