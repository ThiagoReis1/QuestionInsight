from numpy import*
senha = input("senha: ")

i = 0
vogal = 0
outro = 0

while i < len(senha):
	if senha[i] == "A" or senha[i]=="a":
		vogal = vogal + 1
	elif senha[i] == "E" or senha[i]=="e":
		vogal = vogal + 1
	elif senha[i] == "I" or senha[i]=="i":
		vogal = vogal + 1
	elif senha[i] == "O" or senha[i]=="o":
		vogal = vogal + 1
	elif senha [i] == "U" or senha[i]=="u":
		vogal = vogal + 1
	else:
		outro = outro + 1
	i = i + 1
total = vogal * 3.15 + outro * 4.17
print (round(total,2))

#DADO
#0123

#senha[0]= D

