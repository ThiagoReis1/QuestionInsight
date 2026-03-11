r = input("Resposta:")
i = 0
while(r.upper()!="S"):
	if(r.upper()== "SIM"):
		i = i + 1
		r = input("Resposta:")
	else:
		r = input("Resposta:")
print(i)