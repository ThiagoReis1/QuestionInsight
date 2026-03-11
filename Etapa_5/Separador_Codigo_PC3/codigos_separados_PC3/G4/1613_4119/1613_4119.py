from numpy import*
v1 = array(eval(input("nomes das atividades fisicas: ")))
v2 = array(eval(input("duracao das atividades: ")))
v3 = zeros(len(v2), dtype = float)

for i in range(len(v1)):
	if (v1[i] == "ALONGAMENTO"):
		v3[i] = v2[i] * 3.0
	elif (v1[i] == "CORRIDA"):
		v3[i] = v2[i] * 10.3
	elif (v1[i] == "DANCA"):
		v3[i] = v2[i] * 6.7
	elif (v1[i] == "ESCALADA"):
		v3[i] = v2[i] * 9.7
	else:
		v3[i] = v2[i] * 5.0 
s = sum(v3)
print(round(s, 2))
