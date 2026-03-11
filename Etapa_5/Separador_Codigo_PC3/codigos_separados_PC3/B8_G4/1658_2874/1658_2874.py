from numpy import *
paises = input("Digite: ").split(',')
nCHN = 0
nJPN = 0
nKOR = 0
nMGL = 0
nTHA = 0

for i in paises:
	if(i == "CHN"):
		nCHN +=1
	elif(i == "JPN"):
		nJPN +=1
	elif(i == "KOR"):
		nKOR +=1
	elif(i == "MGL"):
		nMGL +=1
	elif(i == "THA"):
		nTHA +=1

vet = array([nCHN,nJPN, nKOR, nMGL, nTHA ])

print(max(vet))
print(vet)		
	