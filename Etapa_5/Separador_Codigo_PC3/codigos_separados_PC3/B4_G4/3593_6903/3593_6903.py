from numpy import *
j = array(eval(input("Insira as jogadas: ")))
t = size(j) - 1
i = 0
j1 = 200

while i <= t:
	if j[i] == 1:
		j1 = j1/2
	elif j[i] == 2:
		j1 = j1*3
	elif j[i] == 3:
		j1 = j1/2
	elif j[i] == 4:
		j1 = j1*3
	elif j[i] == 5:
		j1 = j1/2
	else:
		j1 = j1*3
	i += 1
print(round(j1,2))