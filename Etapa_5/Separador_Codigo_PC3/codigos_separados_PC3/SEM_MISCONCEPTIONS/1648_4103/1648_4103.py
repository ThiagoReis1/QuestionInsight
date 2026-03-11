from numpy import * 
fre = array(eval(input("Frenquencia dos alunos: ")))

rep = 0
for i in range(size(fre)):
	if (fre[i] < 70):
		rep = rep + 1
		
saida = zeros(rep, dtype = int)
rep = 0
for i in range(size(fre)):
	if (fre[i] < 70):
		saida[rep] = i
		rep = rep + 1
			
			
print(rep)
print(saida)