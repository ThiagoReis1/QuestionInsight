# faça seu código aqui!
n = int(input("digite um numnero: "))
#l = input("digite a letra: ").upper()
cont = 0
acmA = 0
acmB = 0
acmC = 0

while (cont < n): 
	l = input("digita a letra: ").upper()
	if (l == "A"):
		acmA = acmA + 1
	elif (l == "B"):
		acmB = acmB + 1
	elif (l == "C"):
		acmC = acmC + 1
	cont = cont + 1
	
print("A= ", acmA)
print("B=", acmB)
print("C=", acmC)
