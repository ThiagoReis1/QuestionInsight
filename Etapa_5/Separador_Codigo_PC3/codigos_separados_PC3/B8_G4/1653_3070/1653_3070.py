from numpy import*
p = input("string: ")

vet = p.split(',')

AR = 0
BR = 0
CL = 0
CO = 0
UY = 0

nvet = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i] == "AR"):
		AR = AR + 1
		nvet[0] = AR
	elif(vet[i] == "BR"):
		BR = BR + 1
		nvet[1] = BR
	elif(vet[i] == "CL"):
		CL = CL + 1
		nvet[2] = CL
	elif(vet[i] == "CO"):
		CO = CO + 1
		nvet[3] = CO
	elif(vet[i] == "UY"):
		UY = UY + 1
		nvet[4] = UY
v = nvet
print(max(v))
print(v)