r1 = input("Digite sim ou nao: ").upper()
i = 0
while (r1!="S"):
	if(r1=="SIM"):
		i = i + 1
	r1 = input("Digite sim ou nao: ").upper()
print(i)