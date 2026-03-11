from numpy import * 
alunos=array(eval(input("Vetor alunos matriculados: ")))
var=zeros(2,dtype=int)
acumu=0

for i in size(alunos):
	if var[i]%0:
		var[0]=var[0]+1
print(var)		
	
