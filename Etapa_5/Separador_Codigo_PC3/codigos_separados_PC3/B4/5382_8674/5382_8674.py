from numpy import*

string = input("coloque as letras: ")
a = 0

for i in range(len(string)):
	if string[i] == "A":
		a = a + .25
	elif string[i] == "E":
		a = a + .25
	elif string[i] == "I":
		a = a + .25
	elif string[i] == "O":
		a = a + .25
	elif string[i] == "U":
		a = a + .25
	else:
		a = a + .27
		
print(round(a , 2))