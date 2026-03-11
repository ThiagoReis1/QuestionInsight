from numpy import *
num = array(eval(input("dados lancados:")))
i = 0
cont = 0
while i < size(num):
	if num[i] == 1:
		cont = cont + 10
	elif num[i] == 2:
		cont = cont + 5
	elif num[i] == 3:
		cont = cont + 10
	elif num[i] == 4:
		cont = cont + 5
	elif num[i] == 5:
		cont = cont + 10
	elif num[i] == 6:
		cont = cont + 5
	i = i + 1
print(round(cont, 10))