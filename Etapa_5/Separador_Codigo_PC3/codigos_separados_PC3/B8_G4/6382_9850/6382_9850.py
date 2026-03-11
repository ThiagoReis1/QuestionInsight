from numpy import*

cod = array(eval(input("Codigo: ")))

for i in range(size(cod)):
	if cod[i] < 9:
		cod[i] = (cod[i] + 1) ** 2
	elif cod[i] == 9:
		cod[i] = 0
print(cod)