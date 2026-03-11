aneis = eval(input("digite o vetor de aneis acertados: "))
total = 0

for i in range(len(aneis)):
	anel = aneis[i]
	if anel == 1:
		total += 100
	elif anel == 2:
		total += 60
	elif anel == 3:
		total += 20
	elif anel == 4:
	   total += 0
print(total)