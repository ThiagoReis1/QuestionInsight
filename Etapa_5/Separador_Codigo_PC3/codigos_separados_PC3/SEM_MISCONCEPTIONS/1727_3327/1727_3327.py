from numpy import*
matriz = array(eval(input("Digite as notas: ")))
maiores=zeros(shape(matriz)[0])
for i in range(shape(matriz)[0]):
	maiores[i] = max(matriz[i,:])
print(max(maiores))