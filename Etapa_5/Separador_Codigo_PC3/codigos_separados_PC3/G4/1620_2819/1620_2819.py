from numpy import *
#vetores de entrada
t = array(eval(input(""))) #tempos do banho (em min)
a = array(eval(input(""))) #percentual de abertura (em %)
#vetor de saída
c = zeros(size(t), dtype=float)
#contadores
i = 0  #indice dos vetores de entrada  
while(i < size(t)):
	c[i] = t[i]*(a[i]/20) 
	i += 1
print(round(sum(c), 2))
