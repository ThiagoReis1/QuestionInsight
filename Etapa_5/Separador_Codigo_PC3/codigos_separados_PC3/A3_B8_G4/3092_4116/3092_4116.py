v = input("Digite o resultado do jogo: ")
t = 0 
V = 3
D = 1
E = 2
l = 1
while (v != "x"):
	v = input("Digite o resultado do jogo: ")
	if (v == "V"):
		t = t + 1
		l = t * 3

	elif (v == "D"):
		t = t + 1
		l = t * 2

	elif (v == "E"):
		t = t + 1
		l = t * 1
		
print(round((l / 10), 2))	
		