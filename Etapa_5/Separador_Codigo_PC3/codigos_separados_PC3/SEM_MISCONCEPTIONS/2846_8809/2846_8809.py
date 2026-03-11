from numpy import*
valor=array(eval(input("ensira um vetor de numeros que vao de 0 a 9: ")))
for i in range(size(valor)):
	valor[i] = valor[i]*2
print(valor)