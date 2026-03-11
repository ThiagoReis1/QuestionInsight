from numpy import *

n=input("Digite as tarefas: ").upper().split(',')

cont=zeros(4,dtype=int)

for i in n :
	if i=='A':
		cont[0]=cont[0]+1
	elif i=='P':
		cont[1]=cont[1]+1
	elif i=='D':
		cont[2]=cont[2]+1
	elif i=='M':
		cont[3]=cont[3]+1
print(cont)
		