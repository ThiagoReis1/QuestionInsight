id = int(input("Idade do espectador: "))

if (id < 12):
	id = 20 + 1.25
	print(id)
	
elif (id == 12):
	id = 20 + 2.25
	print(id)
	
else:
	id = 20 + 3.25
	print(id)