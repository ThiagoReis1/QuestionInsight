from numpy import*
cod = arr
cod = array(eval(input("Codigo: ")))


for i in cod:
	if(i == 0):
		cod[i] = cod[i] + 9
	else:
		cod[i] = cod[i] - 1
print(cod)