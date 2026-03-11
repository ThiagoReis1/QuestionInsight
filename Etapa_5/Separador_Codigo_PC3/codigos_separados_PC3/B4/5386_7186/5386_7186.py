from numpy import*

senha = input("").upper()

i = 0
j = 0

while (i < len(senha)):
	if(senha[i] == "A"):
		j = j + 1.12
	elif(senha[i] == "E"):
		j = j + 1.12
	elif(senha[i] == "I"):
		j = j + 1.12
	elif(senha[i] == "O"):
		j = j + 1.12
	elif(senha[i] == "U"):
		j = j + 1.12
	else:
		j = j + 1.18
	i = i + 1
print(round(j, 2))