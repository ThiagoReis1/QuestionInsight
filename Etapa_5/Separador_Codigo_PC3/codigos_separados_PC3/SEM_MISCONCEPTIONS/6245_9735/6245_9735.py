r = input("reposta: ").upper()
conts = 0
cont = 0
while r!= "X":
	if r == "S":
		cont = cont + 1
		conts = conts + 1
		r = input("resposta: ").upper()
	else:
		cont = cont + 1
		r = input("resposta: ").upper()
print(conts)
	