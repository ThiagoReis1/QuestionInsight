# faça seu código aqui!
n = int(input(" quantidade de funcionarios: "))
#l = float(input("digite o tema: ")).upper()
tecn = 0
tecnA = 0
tecnB = 0
tecnC = 0 

while (tecn < n):
	l = input("digite a letra: ").upper()
	if (l == "A"):
		tecnA = tecnA + 1
	elif (l == "B"):
		tecnB = tecnB + 1
	elif (l == "C"):
		tecnC = tecnC + 1
	tecn = tecn + 1
	
print("A=", tecnA)
print("B=", tecnB)
print("C=", tecnC)


