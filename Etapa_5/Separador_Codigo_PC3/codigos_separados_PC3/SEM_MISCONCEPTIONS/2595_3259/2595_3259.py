from numpy import *
dem = array(eval(input("Dados: ")))
saida=0

for i in range(1, size(dem)):
	if dem[i] <= -dem[0] :
		saida = saida + 1
		print(i)
print(saida)

	
		