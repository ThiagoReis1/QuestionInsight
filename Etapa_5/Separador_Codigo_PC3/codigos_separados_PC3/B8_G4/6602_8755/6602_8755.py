# faça seu código aqui!
n = int(input("digite aqui: "))
cont = 0
acmL = 0
acmC = 0
acmP = 0 

while (cont < n):
	prato = input("digite aqui: ")
	if prato.upper() == "L":
		acmL = acmL + 1
	elif prato.upper() == "C":
		acmC = acmC + 1
	elif prato.upper() == "P":
		acmP = acmP + 1
	cont = cont + 1 
print("L=", acmL)
print("C=", acmC)
print("P=", acmP)
