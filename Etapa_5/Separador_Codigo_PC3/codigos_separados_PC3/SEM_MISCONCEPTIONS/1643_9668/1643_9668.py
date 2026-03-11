from numpy import * 

mf = array(eval(input("notas: ")))
aprovados = 0

for i in range(size(mf)):
	if mf[i] >= 5:
		aprovados = aprovados + 1
		
ind_aprv = zeros(aprovados, dtype = int)
saida = 0 

for i in range(size(mf)):
	if mf[i] >= 5:
		ind_aprv[saida] = i
		saida = saida + 1
		
print(aprovados)
print(ind_aprv)