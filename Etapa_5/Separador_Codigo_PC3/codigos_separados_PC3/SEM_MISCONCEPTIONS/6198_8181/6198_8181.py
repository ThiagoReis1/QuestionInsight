altura_luna = 1.65
taxa_luna = 0.02
A = float(input(": "))
Tc = float(input(": "))
cont = 0

while (A < altura_luna):
	altura_luna = altura_luna + taxa_luna
	A = A+Tc
	cont = cont + 1
	
print(cont)