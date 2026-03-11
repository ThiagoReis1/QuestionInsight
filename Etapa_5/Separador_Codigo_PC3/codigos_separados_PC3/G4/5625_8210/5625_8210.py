TouS = input("Tapioca ou Salgado? ")
q = int(input("Quantidade de tapioca ou salgado: "))
qa = int(input("Quantidade de acais: "))

if TouS.upper() == "T":
	print(q*5.50+qa*10)
else:
	print(q*4+qa*10)