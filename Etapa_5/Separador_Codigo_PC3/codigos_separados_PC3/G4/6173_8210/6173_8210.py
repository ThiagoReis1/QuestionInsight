b = input("sim ou nao: ")
c=0

while b.upper()!="S":
	if b.upper()=="SIM":
		c=c+1
	b = input("sim ou nao: ")
print(c)