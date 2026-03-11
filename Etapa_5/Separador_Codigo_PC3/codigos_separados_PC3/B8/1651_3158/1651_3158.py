from numpy import*

string = input(). split(",")
print(string)

cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

for i in range(len(string)):
	if string[i] == "MC":
		cont = cont + 1
	elif string[i] == "C":
		cont1 = cont1 + 1
	elif string[i] == "CM":
		cont2 = cont2 + 1
	elif string[i] == "EM":
		cont3 = cont3 + 1
	elif string[i] == "E":
		cont4 = cont4 + 1
	elif string[i] == "ME":
		cont5 = cont5 + 1
		
x = array([cont,cont1,cont2,cont3,cont4,cont5])
print(x)

for i in range(len(x)):
	if x[i] == max[x]:
		print(x[i])
