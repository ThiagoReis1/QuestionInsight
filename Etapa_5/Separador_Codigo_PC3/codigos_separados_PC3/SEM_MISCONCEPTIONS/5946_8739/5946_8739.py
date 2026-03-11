qual = input("L/P: ")
quanto = float(input("quantas: "))
quantor = float(input("refrigrante: "))

L = 6
P = 4.5
refr = 3

if qual == "L" :
	valor1 = quanto * L + quantor * refr
	print(round(valor1,2))
	
else:
	valor2 = P * quanto + quantor * refr
	print(round(valor2,2))