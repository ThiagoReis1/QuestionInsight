from numpy import *
j = array(eval(input("jogadas do arrombado: ")))
i = 0
while(i < size(j)):
	if(j[i] == [1]):
		j[i] = j[i] * 80
	elif(j[i] == [2]):
		j[i] = j[i] * 20
	elif(j[i] == [3]):
		j[i] = j[i] * 20 / 3
	elif(j[i] == [4]):
		j[i] = j[i] * 10 / 4
	else:
		j[i] = 0
	i = i + 1
print(sum(j))