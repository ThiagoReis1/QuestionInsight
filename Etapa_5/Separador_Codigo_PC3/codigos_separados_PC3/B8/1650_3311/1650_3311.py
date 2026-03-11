#cor do cabelo
from numpy import*
from math import*
nome = input("Digite:")
vetor = nome.split(',')
vetor_resposta = zeros(5,dtype=int)#numero de cores de cabelo(pele ou estados) disponiveis -> 5
for cont in vetor:
	if(cont.upper()=="P"):
		vetor_resposta[0]=vetor_resposta[0]+1
	elif(cont.upper()=="C"):
		vetor_resposta[1]=vetor_resposta[1]+1
	elif(cont.upper()=="R"):
		vetor_resposta[2]=vetor_resposta[2]+1
	elif(cont.upper()=="L"):
		vetor_resposta[3]=vetor_resposta[3]+1
	elif(cont.upper()=="B"):
		vetor_resposta[4]=vetor_resposta[4]+1
print(max(vetor_resposta))
print(vetor_resposta)



