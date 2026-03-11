from numpy import*
frequencias = array(eval(input()))
num_reprovados = 0
indice_reprovados = []
for i in range(size(frequencias)):
	if frequencias[i] <70:
		num_reprovados +=1
		indice_reprovados = indice_reprovados +[i]
indice_reprovados = array(indice_reprovados)
print(num_reprovados)
print(indice_reprovados)