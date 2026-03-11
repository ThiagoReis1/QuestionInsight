from numpy import *

v = array(eval(input("Coloque as notas finais de cada aluno: ")))

reprovados = 0

for i in range(size(v)):
	if (v[i] < 5.0):
		reprovados = reprovados + 1
		
print(reprovados)	

a = zeros(reprovados, dtype = int)

x = 0

for j in range(size(v)):
	if (v[j] < 5.0):
		a[x] = j 
		x = x + 1
		
print(a)