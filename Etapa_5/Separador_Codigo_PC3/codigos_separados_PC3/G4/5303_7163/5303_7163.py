mat = int(input("insira o material: "))

cont = 0

while mat >= 0.5:
	mat = mat - (mat * (10/100))
	cont = cont + 1
	
print(cont)