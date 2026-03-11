pontos = input()
v = 0
e = 0
while(pontos.upper() != "X"):
	if(pontos.upper() == "V"):
		v = v + 3
	elif(pontos.upper() == "E"):
		e = e + 1
	pontos = input()
print(v)
print(e)