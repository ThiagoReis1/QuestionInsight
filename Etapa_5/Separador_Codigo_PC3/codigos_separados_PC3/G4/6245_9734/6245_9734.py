cont = 0
resp = input("resposta").upper

while resp!= "X":
	if resp == "S":
			cont += 1
			resp = input("resposta").upper
print(cont)
