o = input()
cont = 0
while o.upper() != "X":
	if o.upper() == "S":
		cont = cont + 1
	o = input()
print(cont)