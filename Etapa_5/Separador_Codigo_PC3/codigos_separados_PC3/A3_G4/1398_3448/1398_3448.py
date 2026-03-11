tempo = float(input("informe o tempo em minutos"))


t1 = (tempo - 200)
pf1 = 5000 + (tempo*100)
t2 = (tempo - 200)
pf2 = 8000 + (100*200)  + (t2*90)

if (tempo <= 200):
	
	print(round(pf1,2))
	
else:
	print(round(pf2,2))
	