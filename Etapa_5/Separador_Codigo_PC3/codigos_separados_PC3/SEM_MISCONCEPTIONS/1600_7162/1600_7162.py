# Importar o módulo de vetor
from numpy import *

# Leitura do vetor
custo = array(eval(input("Digite o vetor com os custos:")))

i=0 # variável contadora
s=0 # variáavel acumuladora

while i<size(custo):
	if custo[i]>80:
		s = s + (custo[i]-0.15*custo[i])
		i=i+1
	else:
		s = s + custo[i]
		i=i+1
		
print(round(s,2))		