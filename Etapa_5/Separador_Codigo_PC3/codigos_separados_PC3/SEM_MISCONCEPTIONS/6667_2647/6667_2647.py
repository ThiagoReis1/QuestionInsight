from numpy import *
entrada = []
for i in range(10):
	entrada.append(float(input()))
ap = float(input())
vaprovados= []
aprovados =0
for i in range(len(entrada)):
	if(entrada[i]>=0 and entrada[i]<=10):
		if(entrada[i]>=ap):
			vaprovados.append(entrada[i])
			aprovados+=1
vazio = zeros(aprovados, dtype=float)
for i in range(aprovados):
	vazio[i]=vaprovados[i]
print(aprovados)
print(vazio)