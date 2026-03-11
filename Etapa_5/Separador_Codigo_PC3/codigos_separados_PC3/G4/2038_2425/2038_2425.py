a = input("resposta:")
a = a.upper()
i = 0
while(a == 'SIM' or a=='NAO'):
	if(a == 'SIM'):
		i = i + 1
	a = input("resposta:")
	a = a.upper()
if(a == 'S'):
	print(i)
	