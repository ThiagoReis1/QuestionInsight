#Universidade Federal do Amazonas
#Aluna: Ingrid de Lira Lima
#Exercicio: 01

from numpy import*
vetor= array(eval(input("digite os valores: "))) 
i=0
j=0
while i< size(vetor):
	if  (vetor[i]> -60) and (vetor[i]< 60):
		j= j+1
	i=i+1
vetorl= array(zeros(j,dtype=float))
i=0
j=0
while i< size(vetor):
	if  (vetor[i]> -60) and (vetor[i]< 60):
		vetorl[j] = vetor[i]
		j= j+1
	i = i+1
print(vetorl)
		
		
		
	
		
		
		
		
		
		
		