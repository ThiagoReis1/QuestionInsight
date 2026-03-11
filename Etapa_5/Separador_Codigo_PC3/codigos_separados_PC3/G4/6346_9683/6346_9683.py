v1 = input("Coloque seu nome: ")

i = 0 
t = len(v1) - 1

while i <= t:
	if v1[0] == "W":
		print (v1.upper())
		break
	else:
		print("nome invalido")
		break