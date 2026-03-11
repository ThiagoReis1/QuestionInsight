from numpy import *

estados = input()
vetEst = estados.split(',')
contAm = 0
contPe = 0
contMg = 0
contSp = 0
contRs = 0

for i in range(len(vetEst)):
	if vetEst[i] == "AM":
		contAm+=1
	if vetEst[i] == "PE":
		contPe+=1
	if vetEst[i] == "MG":
		contMg+=1
	if vetEst[i] == "SP":
		contSp+=1
	if vetEst[i] == "RS":
		contRs+=1

vetPessoas = [0]*5
vetPessoas[0] = contAm
vetPessoas[1] = contPe
vetPessoas[2] = contMg
vetPessoas[3] = contSp
vetPessoas[4] = contRs

maior = vetPessoas[0]
for i in range(1,len(vetPessoas)):
	if(vetPessoas[i] > maior):
		maior = vetPessoas[i]

print(maior)
print(array(vetPessoas))
