from numpy import array, size
dado = array(eval(input()))
i = 0
cont = 0
while i < (size(dado)):
	if dado[i] == 1:
		cont += 10
	elif dado[i] == 2:
		cont += 5
	elif dado[i] == 3:
		cont += 0
	elif dado[i] == 4:
		cont += 5
	elif dado[i] == 5:
		cont += 20
	elif dado[i] == 6:
		cont += 10
	i += 1
print(cont)