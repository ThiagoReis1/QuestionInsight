v = input(" ")

i = 0
D = 0
S = 0
I = 0
cont = 0

while (i < len(v)):
	if (v[i] == "D"):
		D = D + 1
		cont = cont + 2.25
	elif (v[i] == "S"):
		S = S + 1
		cont = cont + 4.0
	elif (v[i] == "I"):
		I = I + 1
		cont = cont + 6.90
		
	i = i + 1
print(round(cont,2), D,S,I)
