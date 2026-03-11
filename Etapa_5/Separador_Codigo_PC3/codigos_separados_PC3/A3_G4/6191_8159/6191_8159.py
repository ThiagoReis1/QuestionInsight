x=input("CARA ou COROA").upper()
cont=0
y=0
while x != "S":
	if x == "CARA" :
		cont += 1
	else:
		y += 1
	x=input("CARA ou COROA").upper()
print(cont)