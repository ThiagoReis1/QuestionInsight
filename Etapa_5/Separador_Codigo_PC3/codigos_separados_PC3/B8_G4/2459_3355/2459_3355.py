p = float(input("Peso: "))
d = float(input("Distancia: "))
c = input("Codigo do estado de destino: ")

p = p*25
d = d*0.1

if (c == "1"):
	s = (p+d)*(1+(17/100))
	print(round(s, 2))
elif (c == "2"):
	s = (p+d)*(1+(17.5/100))
	print(round(s, 2))
elif (c == "3"):
	s = (p+d)*(1+(18/100))
	print(round(s, 2))
elif (c == "4"):
	s = (p+d)*(1+(20/100))
	print(round(s, 2))
