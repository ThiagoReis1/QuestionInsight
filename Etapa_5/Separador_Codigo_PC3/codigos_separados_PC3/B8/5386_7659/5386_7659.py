from numpy import*

senha = input("digite: ")

i = 0
k = 0
j = 0

while(i <len(senha)):
	if(senha[i].upper() == "A" or senha[i].upper() == "E" or senha[i].upper() == "I" or senha[i].upper() == "O" or senha[i].upper() == "U"):
		k = k + 1
	elif(senha[i].upper() != "A" or senha[i].upper() != "E" or senha[i].upper() != "I" or senha[i].upper() != "O" or senha[i].upper() != "U"):
		j = j + 1
	i = i + 1
	total = (k*1.12) + (j * 1.18)
print(round(total, 2))