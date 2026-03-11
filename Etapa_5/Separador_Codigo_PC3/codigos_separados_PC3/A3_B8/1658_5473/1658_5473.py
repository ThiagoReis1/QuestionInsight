from numpy import *
cont = zeros(5, dtype=int)
maior = 0
paises = input("quantidade de pessoas de cada pais: ").upper().split(',')
	
for i in range(size(paises)):
	if(paises[i]=='CHN'):
		cont[0] = cont[0] + 1
	elif(paises[i]=='JPN'):
		cont[1] = cont[1] + 1
	elif(paises[i]=='KOR'):
		cont[2]=cont[2] + 1
	elif(paises[i]=='MGL'):
		cont[3]=cont[3] + 1
	elif(paises[i]=='THA'):
		cont[4]=cont[4]+1

print(max(cont))
print(cont)