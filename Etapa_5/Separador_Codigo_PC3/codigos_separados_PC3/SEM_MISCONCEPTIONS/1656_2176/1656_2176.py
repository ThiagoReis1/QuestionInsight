from numpy import *
vetp = input("Digite o pais").split(',')
i = 0
vetNP = zeros(5, dtype=int)
while(i<size(vetp)):
	if(vetp[i] == "BE"):
		vetNP[0] = vetNP[0] + 1
	elif(vetp[i] == "ES"):
		vetNP[1] = vetNP[1] + 1
	elif(vetp[i] == "FR"):
		vetNP[2] = vetNP[2] + 1
	elif(vetp[i] == "IT"):
		vetNP[3] = vetNP[3] + 1
	else:
		vetNP[4] = vetNP[4] + 1
	i = i + 1
print(max(vetNP))
print(vetNP)