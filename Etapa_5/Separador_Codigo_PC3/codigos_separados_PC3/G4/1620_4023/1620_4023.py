from numpy import *

v1 = array(eval(input("Digite o vetor com os tempos dos banhos(em minutos): ")))
v2 = array(eval(input("Digite o vetor com o percentual de abertura da torneira: ")))

cont = 0

for i in range(size(v1)):
	cont = cont + (v1[i]*((v2[i]/100)*5))
	
print(round(cont, 2))