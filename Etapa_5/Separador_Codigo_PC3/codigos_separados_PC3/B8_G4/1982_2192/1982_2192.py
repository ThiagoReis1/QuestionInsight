p = input()
c = input()

if((p == "Italia" or p == "Espanha") and (c == "Roma" or c == "Florenca" or c == "Frigiliana" or c == "Madrid")):
	if(p == "Italia" and c == "Roma"):
		pr = "latina".upper()
		print(pr)
	elif(p == "Italia" and c == "Florenca"):
		pr = "siena".upper()
		print(pr)
	elif(p == "Espanha" and c == "Frigiliana"):
		pr = "malaga".upper()
		print(pr)
	elif(p == "Espanha" and c == "Madrid"):
		pr = "madrid".upper()
		print(pr)
else:
	i = "provincia nao identificada".upper()
	print(i)
		