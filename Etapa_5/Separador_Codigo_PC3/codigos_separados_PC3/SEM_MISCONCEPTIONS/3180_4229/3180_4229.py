from numpy import*
vetor = array(eval(input("lista de sorotipos dos pacientes: ")))
doentes = zeros(4,int)
for i in range(size(vetor)):
	if(vetor[i]==1):
		doentes[0] = doentes[0] + 1
	if(vetor[i]==2):
		doentes[1] = doentes[1] + 1
	if(vetor[i]==3):
		doentes[2] = doentes [2] + 1
	if(vetor[i]==4):
		doentes[3]=doentes[3] + 1
print(doentes)