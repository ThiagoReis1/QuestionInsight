

12

from numpy import *
#vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

q_m = array(eval(input("Informe a quantidade de presentes no curso: ")))
q_f = array(eval(input("Informe a quantidade de  no curso: ")))

p = []
i = 0
k = 0

while( i < size(q_m)):
	p.append(q_m[i] - q_f[i])
	
	i += 1
	
while(p[k] != max(p)):
	k += 1
	
print(k + 1)		
