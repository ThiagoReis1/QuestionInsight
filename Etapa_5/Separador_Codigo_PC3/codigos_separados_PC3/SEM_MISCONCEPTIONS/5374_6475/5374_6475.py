from numpy import *
name= input('type here: ')

tamanho= len(name)
i= 0
custo= 0

while(i<tamanho):
	if ((name[i]=='A') or (name[i]=='E') or (name[i]=='I') or (name[i]=='O') or (name[i]=='U')):
		custo= custo+0.15
		i= i+1
	else:
		custo= custo+0.17
		i= i+1
		
print(round(custo, 2))