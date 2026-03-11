molec = input()
mol = molec.upper()

if mol == "GLUTAMINA":
		peso = 5*12.011 + 8*1.00794 + 1*14.0067 + 4*15.9994
		print (round(peso, 2))
elif mol == "SERINA":
	peso = 3*12.011 + 7*1.00794 + 14.0067 + 3*15.9994
	print (round(peso, 2))
elif mol == "TREONINA":
	peso = 4*12.011 + 9*1.00794 + 14.0067 + 3*15.9994
	print (round(peso, 2))
else:
	print("Entrada:", mol)
	print("Dado Invalido")