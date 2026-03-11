from numpy import *
matriz = (array(eval(input("matriz: "))))
col = shape(matriz)[1]
vet = zeros(col, dtype=float)
for i in range(col):
	vet[i] = min(matriz[:,i])
print(min(vet))






#matriz = array(eval(input("matriz: ")))
#vet = zeros(3, dtype=float)
#menor1 = min(matriz[:,0])
#menor2 = min(matriz[:,1])
#menor3 = min(matriz[:,2])
#vet[0] = menor1
#vet[1] = menor2
#vet[2] = menor3
#print(min(vet))

#matriz[1,1]
#print(matriz[1,1])

#col = shape(matriz)[1]
#for j in range(col):
#	menor = min(col[:,j]
#print(menor)

#while(col[i] != min(col[i])):
#	i = i + 1
#print(col[i])