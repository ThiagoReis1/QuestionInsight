from numpy import *
name= input(':')

tamanho= len(name)
i= 0
custo= 0

while(i<tamanho):
	if ((name[i]=='A') or (name[i]=='E') or (name[i]=='I') or (name[i]=='O') or (name[i]=='U')):
		custo= custo+1.12
		i= i+1
	else:
		custo= custo+1.18
		i= i+1
		
print(round(custo, 2))